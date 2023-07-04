# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

import fire
import json
import os
from collections import defaultdict
from graphlib import TopologicalSorter

OUT_DIR = 'generated'
MODEL_SNAPSHOT = os.path.join(OUT_DIR, 'modelTypes.json')

typemap = {
    'xsd:anyURI': 'str',
    'xsd:integer': 'int',
    'xsd:string': 'str'
}


def write_tools_class(model, mtypes, out):
    meta = mtypes[model]['Metadata']
    for m in meta:
        assert m in {'name', 'SubclassOf', 'Instantiability',
                     '_modelRef', '_profile', '_category', '_file'}

    pdir = os.path.join(out, meta['_profile'])
    os.makedirs(pdir, exist_ok=True)
    class_name = meta['name']
    parent_name = meta.get('SubclassOf', '')
    with open(os.path.join(pdir, meta['name']) + '.py', 'w') as fp:
        if meta['_category'] == 'Classes':
            fp.write(f'class {class_name}:\n')
            for k, v in mtypes[model]['Properties'].items():
                ptype = typemap.get(v['type'], v['type'])
                fp.write(f'    {k}: {ptype} = None\n')
        elif meta['_category'] == 'Vocabularies':
            fp.write(f'class {class_name}(Enum):\n')
            for n, v in enumerate(mtypes[model]['Entries'], start=1):
                fp.write(f'    {v} = {n}\n')


def subclass(td):
    return td['Metadata'].get('SubclassOf', '').split('/')[-1]


# Fill in or update properties from superclass
def build_td(tname, model_types):
    if td := model_types.get(tname, {}):
        if 'Properties' in td:
            # Apply default property constraints
            for k, tdp in td['Properties'].items():
                p = {'minCount': 0, 'maxCount': '*'}
                p.update(tdp)
                if p['maxCount'] != '*':
                    assert int(p['minCount']) <= int(p['maxCount'])
                td['Properties'][k] = p
            # Propagate properties to subclasses
            if sd := model_types.get(subclass(td), {}):     # TODO: generate list types
                for k, p in sd['Properties'].items():
                    if k in td['Properties'] and p != td['Properties'][k]:
                        tdp = td['Properties'][k]    # ensure restrictions
                        assert tdp['type'] == p['type']
                        assert int(tdp['minCount']) >= int(p['minCount'])
                        if p['maxCount'] != '*':
                            assert int(tdp['maxCount']) <= int(p['maxCount'])
                    td['Properties'][k] = p
    return td


def make_types(model: str = MODEL_SNAPSHOT, out: str = OUT_DIR) -> None:
    # Load model snapshot created by "parse_model"
    with open(model) as fp:
        model_types = json.load(fp)

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
