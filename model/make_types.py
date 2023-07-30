# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

import copy
import fire
import json
import os
from collections import defaultdict
from graphlib import TopologicalSorter

OUT_DIR = 'generated'
MODEL_SNAPSHOT = 'modelTypes.json'

# Model types to be serialized as references, not inlined
typerefs = {
    "Element": "SpdxId"
}

# List datatypes and logical type names
datatypes = {
    'xsd:string': 'String',
    'xsd:integer': 'Integer',
    'xsd:anyURI': 'AnyUri'
}

python_class = {
    'String': 'str',
    'Integer': 'int',
}

# Type definitions to patch missing classes in model
model_patches = {
    'String': {
        'Summary': {},
        'Description': {},
        'Metadata': {
            'name': 'String',
            '_profile': 'Core',
            '_category': 'Datatypes',
            '_file': 'String.md',
            '_html': '',
            '_generated': True
        },
        'Format': {
            'schema': 'xsd:string'
        }
    },
    'Integer': {
        'Summary': {},
        'Description': {},
        'Metadata': {
            'name': 'Integer',
            '_profile': 'Core',
            '_category': 'Datatypes',
            '_file': 'Integer.md',
            '_html': '',
            '_generated': True
        },
        'Format': {
            'schema': 'xsd:integer'
        }
    },
    'AnyUri': {
        'Summary': {},
        'Description': {},
        'Metadata': {
            'name': 'AnyUri',
            'SubclassOf': 'String',
            '_modelRef': 'https://rdf.spdx.org/v3/Core/AnyUri',
            '_profile': 'Core',
            '_category': 'Datatypes',
            '_file': 'AnyUri.md',
            '_html': '',
            '_generated': True
        },
        'Format': {
            'schema': 'xsd:anyURI'
        }
    }
}


def write_tools_class(tname, mtypes, out):
    tdef = mtypes[tname]
    meta = tdef['Metadata']
    assert meta['name'] == tname, f'{tname}: Metadata name mismatch {meta["name"]}'
    for m in meta:
        assert m in {'name', 'SubclassOf', 'Instantiability',
                     '_modelRef', '_profile', '_category', '_file', '_html', '_generated', '_root_class'}

    pdir = os.path.join(out, meta['_profile'])
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, meta['name']) + '.md', 'w') as fp:
        commit = f'[{mtypes["_commit"]["url"].split("/")[-1][:7]}]({mtypes["_commit"]["html_url"]})'
        fp.write(f'## [{tname}]({meta["_html"]})\nModel: {commit} {mtypes["_commit"]["date"]}\n```\n')
        supertype = datatypes.get(sc := meta.get("SubclassOf", ''), sc)
        fp.write(f'class {tname}({supertype}):\n')
        if meta['_category'] == 'Classes':
            assert 'Format' not in tdef, f'Complex class {tname} cannot have formats'
            for k, v in tdef.get('Properties', {}).items():
                ptype = datatypes.get(v['type'], v['type']).split('/')[-1]
                rc = mtypes.get(ptype, {}).get('Metadata', {}).get('_root_class', '')
                ptype = typerefs.get(rc, ptype)                 # Use SpdxId for all Element subclasses
                ptype = 'SpdxId' if k == 'spdxId' else ptype
                prop = f'{k}: {ptype} = None'
                opt = ' optional' if str(v['minCount']) == '0' else ''
                pmin = v['minCount'] if (pmax := v['maxCount']) == '1' else '1'
                mult = f'Set[{pmin}..{pmax}]' if pmax != '1' else ''
                gen = mtypes.get(ptype, {}).get('Metadata', {}).get('_generated', False)    # flag patches with '*'
                fp.write(f'    {prop:50} #{" *" if gen else ""}{opt} {mult}\n')
        elif meta['_category'] == 'Datatypes':
            assert 'Properties' not in tdef, f'Simple datatype {tdef} cannot have properties'
            for k, v in tdef['Format'].items():
                if k in ['pattern', 'schema']:
                    # assert supertype == 'String', f'{supertype} does not support {k}'
                    fp.write(f'    {k}: {v}\n')
                else:
                    assert f'Unknown format {k} in {tdef}'
        elif meta['_category'] == 'Vocabularies':
            for n, v in enumerate(tdef['Entries'], start=1):
                fp.write(f'    {v} = {n}\n')
        fp.write('```\n')


def superclass(td):
    return td['Metadata'].get('SubclassOf', '').split('/')[-1]


# Fill in or update properties from superclass
def build_td(tname, model_types):
    if td := model_types.get(tname, {}):
        sd = model_types.get(superclass(td), {})
        k = '_root_class'   # Track types to be serialized as references rather than values
        td['Metadata'].update({k: tname}) if tname in typerefs else {}
        td['Metadata'].update({k: sd['Metadata'][k]} if sd.get('Metadata', {}).get(k, '') else {})

        if td['Metadata']['_category'] in 'Classes':
            if 'Properties' not in td:
                td['Properties'] = {}
            # Apply default property constraints
            for k, tdp in td['Properties'].items():
                p = {'minCount': 0, 'maxCount': '*'}
                p.update(tdp)
                if p['maxCount'] != '*':
                    assert int(p['minCount']) <= int(p['maxCount'])
                td['Properties'][k] = p

            # Propagate properties to subclasses, apply direct restrictions
            for k, p in sd.get('Properties', {}).items():
                if k in td.get('Properties', {}) and p != td['Properties'][k]:
                    tdp = td['Properties'][k]    # ensure restrictions are valid
                    assert tdp['type'] == p['type'], f'Property type mismatch: {tname} {tdp["type"]} != {p["type"]}'
                    assert int(tdp['minCount']) >= int(p['minCount']),\
                        f'Cannot relax constraint: {tname} minCount {p["minCount"]} -> {tdp["minCount"]}'
                    if p['maxCount'] != '*':
                        assert int(tdp['maxCount']) <= int(p['maxCount']),\
                            f'Cannot relax constraint: {tname} maxCount {p["maxCount"]} -> {tdp["maxCount"]}'
                    p = tdp
                td['Properties'][k] = p

            # Apply property restrictions specified indirectly
            for k, r in td.get('External properties restrictions', {}).items():
                assert len(kf := k.split('/')) == 4, f'Invalid property restriction {k}'
                if not (tdp := td.get('Properties', {})):
                    raise ValueError(f'Restricting non-existent property {k} in {td["Metadata"]["name"]}')
                for p, v in r.items():
                    pn = dict(tdp[kf[-1]])  # Make a modifiable copy
                    pn[p] = v
                    tdp[kf[-1]] = pn

        elif td['Metadata']['_category'] in 'Datatypes':
            # Propagate simple datatype definitions to subclasses
            fmt = {k: v for k, v in sd.get('Format', {}).items()}     # make a copy
            fmt.update(td.get('Format', {}))
            if fmt:
                td.update({'Format': fmt})
    return td


def make_types(model: str = MODEL_SNAPSHOT, out: str = OUT_DIR) -> None:
    # Load model snapshot created by "parse_model"
    with open(os.path.join(out, model)) as fp:
        model_types = json.load(fp)
    model_types.update(model_patches)

    # Check consistency
    for k, v in model_types.items():
        if not k.startswith('_'):
            assert k == v['Metadata']['name'], f'{k} name mismatch'

    # Update model_types to full type definitions after subclassing
    refs = defaultdict(list)
    [refs[superclass(t)].append(t['Metadata']['name']) for k, t in model_types.items() if not k.startswith('_')]
    [build_td(t, model_types) for t in reversed([e for e in TopologicalSorter(refs).static_order()])]

    print('Subclass tree:')
    for k, v in refs.items():
        print(f'{k:>30}: [{", ".join(v)}]')

    # Write class files for each type definition
    for td in model_types:
        if not td.startswith('_'):
            write_tools_class(td, model_types, out)


if __name__ == '__main__':
    fire.Fire(make_types)
