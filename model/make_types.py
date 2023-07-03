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
        fp.write(
            f'# SPDX-FileCopyrightText: 2023 spdx contributors\n'
            f'#\n'
            f'# SPDX-License-Identifier: Apache-2.0\n'
            f'from dataclasses import dataclass, field\n'
            f'from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties\n'
            f'from spdx_tools.common.typing.type_checks import check_types_and_set_values\n'
            f'from spdx_tools.spdx3.model import CreationInfo, Element\n'
            f'\n\n'
            f'@dataclass\n'
            f'class {class_name}():\n'
        )
        if meta['_category'] == 'Classes':
            for k, v in mtypes[model]['Properties'].items():
                fp.write(
                    f'    {k}: {v["type"]}\n'
                )


def subclass(td):
    return td['Metadata'].get('SubclassOf', '').split('/')[-1]


# Fill in or update properties from superclass
def build_td(tname, model_types):
    if td := model_types.get(tname, {}):
        if 'Properties' in td:
            for k, tdp in td['Properties'].items():
                p = {'minCount': 0, 'maxCount': '*'}
                p.update(tdp)
                td['Properties'][k] = p
            if sd := model_types.get(subclass(td), {}):     # TODO: generate list types
                for k, p in sd['Properties'].items():
                    if k in td['Properties'] and p != td['Properties'][k]:
                        tdp = td['Properties'][k]    # ensure restrictions
                        assert tdp['type'] == p['type']
                    td['Properties'][k] = p
        if 'Entries' in td:
            pass    # process enumerated types
    return td


def make_types(model: str = MODEL_SNAPSHOT, out: str = OUT_DIR) -> None:
    # Load model snapshot created by "parse_model"
    with open(model) as fp:
        model_types = json.load(fp)

    # Update model_types to full type definitions after subclassing
    refs = defaultdict(list)
    [refs[subclass(t)].append(t['Metadata']['name']) for t in model_types.values()]
    [build_td(t, model_types) for t in reversed([e for e in TopologicalSorter(refs).static_order()])]

    print('Subclass tree:')
    for k, v in refs.items():
        print(f'{k:>30}: [{", ".join(v)}]')

    # Write class files for each type definition
    for n, td in enumerate(model_types):
        if td:
            write_tools_class(td, model_types, out)


if __name__ == '__main__':
    fire.Fire(make_types)
