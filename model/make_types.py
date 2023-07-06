# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

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

# Map from xsd types to Python built-in or model-defined types
typemap = {
    'xsd:anyURI': 'AnyUri',
    'xsd:integer': 'int',
    'xsd:string': 'str'
}

# Type definitions to patch missing classes in model
model_patches = {
    'AnyUri': {
        'Summary': {},
        'Description': {},
        'Metadata': {
            'name': 'AnyUri',
            'SubclassOf': 'none',
            '_modelRef': 'https://rdf.spdx.org/v3/Core/AnyUri',
            '_profile': 'Core',
            '_category': 'Classes',
            '_file': 'AnyUri.md',
            '_html': '',
            '_generated': True
        },
        'Properties': {}
    },
    'SpdxId': {
        'Summary': {},
        'Description': {},
        'Metadata': {
            'name': 'SpdxId',
            'SubclassOf': 'none',
            '_modelRef': 'https://rdf.spdx.org/v3/Core/SpdxId',
            '_profile': 'Core',
            '_category': 'Classes',
            '_file': 'SpdxId.md',
            '_html': '',
            '_generated': True
        },
        'Properties': {}
    }
}


def write_tools_class(model, mtypes, out):
    meta = mtypes[model]['Metadata']
    for m in meta:
        assert m in {'name', 'SubclassOf', 'Instantiability',
                     '_modelRef', '_profile', '_category', '_file', '_html', '_generated', '_root_class'}

    pdir = os.path.join(out, meta['_profile'])
    os.makedirs(pdir, exist_ok=True)
    class_name = meta['name']
    with open(os.path.join(pdir, meta['name']) + '.md', 'w') as fp:
        commit = f'[{mtypes["_commit"]["url"].split("/")[-1][:7]}]({mtypes["_commit"]["html_url"]})'
        fp.write(f'## [{class_name}]({meta["_html"]})\nModel: {commit} {mtypes["_commit"]["date"]}\n```\n')
        if meta['_category'] == 'Classes':
            fp.write(f'class {class_name}:\n')
            for k, v in mtypes[model]['Properties'].items():
                ptype = typemap.get(v['type'], v['type'])
                rc = mtypes.get(ptype, {}).get('Metadata', {}).get('_root_class', '')
                ptype = typerefs.get(rc, ptype)                 # Use SpdxId for all Element subclasses
                ptype = 'SpdxId' if k == 'spdxId' else ptype    # Patch until Element fixed in model
                prop = f'{k}: {ptype} = None'
                opt = ' optional' if str(v['minCount']) == '0' else ''
                pmin = v['minCount'] if (pmax := v['maxCount']) == '1' else '1'
                mult = f'Set[{pmin}..{pmax}]' if pmax != '1' else ''
                fp.write(f'    {prop:50} #{opt} {mult}\n')
        elif meta['_category'] == 'Vocabularies':
            fp.write(f'class {class_name}(Enum):\n')
            for n, v in enumerate(mtypes[model]['Entries'], start=1):
                fp.write(f'    {v} = {n}\n')
        fp.write('```\n')


def subclass(td):
    return td['Metadata'].get('SubclassOf', '').split('/')[-1]


# Fill in or update properties from superclass
def build_td(tname, model_types):
    if td := model_types.get(tname, {}):
        sd = model_types.get(subclass(td), {})
        td['Metadata'].update({'_root_class': tname}) if tname in typerefs else {}
        td['Metadata'].update({k: v for k, v in sd.get('Metadata', {}).items() if k == '_root_class'})
        if 'Properties' in td:
            # Apply default property constraints
            for k, tdp in td['Properties'].items():
                p = {'minCount': 0, 'maxCount': '*'}
                p.update(tdp)
                if p['maxCount'] != '*':
                    assert int(p['minCount']) <= int(p['maxCount'])
                td['Properties'][k] = p
            # Propagate properties to subclasses
            if sd:
                for k, p in sd['Properties'].items():
                    if k in td['Properties'] and p != td['Properties'][k]:
                        tdp = td['Properties'][k]    # ensure restrictions
                        assert tdp['type'] == p['type'], f'Property type mismatch: {tname} {tdp["type"]} != {p["type"]}'
                        assert int(tdp['minCount']) >= int(p['minCount']),\
                            f'Cannot relax constraint: {tname} minCount {p["minCount"]} -> {tdp["minCount"]}'
                        if p['maxCount'] != '*':
                            assert int(tdp['maxCount']) <= int(p['maxCount']),\
                                f'Cannot relax constraint: {tname} maxCount {p["maxCount"]} -> {tdp["maxCount"]}'
                        p = tdp
                    td['Properties'][k] = p
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
    [refs[subclass(t)].append(t['Metadata']['name']) for k, t in model_types.items() if not k.startswith('_')]
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
