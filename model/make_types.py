# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

import fire
import json
import os
from collections import defaultdict
from graphlib import TopologicalSorter

MODEL = 'generated/modelTypes.json'
OUT = 'generated'


def write_tools_class(model, mtypes, out):
    for m in model['Metadata']:
        assert m in {'name', 'SubclassOf', 'Instantiability',
                     '_modelRef', '_profile', '_category', '_file'}

    pdir = os.path.join(out, model['Metadata']['_profile'])
    os.makedirs(pdir, exist_ok=True)
    class_name = model['Metadata']['name']
    parent_name = model['Metadata'].get('SubclassOf', '')
    # if model['Metadata']['_category'] != 'Vocabularies':
        # print(f'{parent_name:36} {class_name}')
    imported = [parent_name]
    with open(os.path.join(pdir, model['Metadata']['name']) + '.py', 'w') as fp:
        fp.write(
            f'# SPDX-FileCopyrightText: 2023 spdx contributors\n'
            f'#\n'
            f'# SPDX-License-Identifier: Apache-2.0\n'
            f'from dataclasses import field\n'
            f'from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties\n'
            f'from spdx_tools.common.typing.type_checks import check_types_and_set_values\n'
            f'from spdx_tools.spdx3.model import CreationInfo, Element\n'
            f'\n\n'
            f'@dataclass_with_properties\n'
            f'class {class_name}({parent_name}):\n'
            f'    def __init__(\n'
            f'        self,\n'
        )
        if model['Metadata']['_category'] == 'Classes':
            for k, v in model['Properties'].items():
                pass    # generate properties

        fp.write(
            f'    ):\n'
            f'        check_types_and_set_values(self, locals())\n'
        )


def build_tdef(tname, model_types):
    tdef = model_types.get(tname, {})
    return tdef


def make_types(model: str = MODEL, out: str = OUT) -> None:
    def subclass(td):
        return td['Metadata'].get('SubclassOf', '').split('/')[-1]

    # Load model snapshot created by "parse_model"
    with open(model) as fp:
        model_types = json.load(fp)

    # Create full type definitions after subclassing
    refs = defaultdict(list)
    [refs[subclass(t)].append(t['Metadata']['name']) for t in model_types.values()]
    tdefs = [build_tdef(e, model_types) for e in reversed([e for e in TopologicalSorter(refs).static_order()])]

    for k, v in refs.items():
        print(f'{k:>30}: {v}')

    # Write class files for each type definition
    for n, td in enumerate(tdefs):
        if td:
            write_tools_class(td, model_types, out)


if __name__ == '__main__':
    fire.Fire(make_types)
