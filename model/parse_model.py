# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

import fire
import json
import os
import re
from io import TextIOWrapper
from typing import TextIO
from urllib.request import urlopen, Request
from urllib.parse import urlparse

SPDX_MODEL = 'https://api.github.com/repos/spdx/spdx-3-model/contents/model'
OUTDIR = 'generated'


class WebDirEntry:
    """
    Fake os.DirEntry type for GitHub filesystem
    """
    def __init__(self, name: str, path: str, url: str, html: str):
        self.name = name
        self.path = path
        self.url = url
        self.html = html


def list_dir(dirpath: str) -> dict:
    """
    Return a dict listing the files and directories in a directory on local filesystem or GitHub repo.

    :param dirpath: str - a filesystem path or GitHub API URL
    :return: dict {files: [DirEntry*], dirs: [DirEntry*]}
    Local Filesystem: Each list item is an os.DirEntry structure containing name and path attributes
    GitHub Filesystem: Each list item has name, path, and url (download URL) attributes
    """

    files, dirs = [], []
    u = urlparse(dirpath)
    if all([u.scheme, u.netloc]):
        with urlopen(Request(dirpath, headers=AUTH)) as d:
            for dl in json.loads(d.read().decode()):
                url = 'url' if dl['type'] == 'dir' else 'download_url'
                entry = WebDirEntry(dl['name'], dl[url], dl['url'], dl['html_url'])
                (dirs if dl['type'] == 'dir' else files).append(entry)
    else:
        with os.scandir(dirpath) as dlist:
            for entry in dlist:
                (dirs if os.path.isdir(entry) else files).append(entry)
    return {'files': files, 'dirs': dirs}


def open_file(fileentry: os.DirEntry) -> TextIO:
    u = urlparse(fileentry.path)
    if all([u.scheme, u.netloc]):
        return TextIOWrapper(urlopen(Request(fileentry.path, headers=AUTH)), encoding='utf8')
    return open(fileentry.path, 'r', encoding='utf8')


def load_model(fp):
    model = {}
    cursor = []
    for line in fp.readlines():
        if m := re.match(r'^\s*##\s*(.+?)(\s*)$', line):
            model[c := m.group(1)] = {}
            cursor = [model[c]]
        elif m := re.match(r'^[-*]\s*([-/\w]+):\s*(.*?)\s*$', line):
            cursor[0].update({m.group(1): m.group(2)})
        elif m := re.match(r'^[-*]\s*([-/\w]+)\s*$', line):
            cursor[0][c := m.group(1)] = {}
            cursor = [cursor[0], cursor[0][c]]
        elif m := re.match(r'^\s+[-*]\s*([-/\w]+):\s*(.*?)\s*$', line):
            cursor[1].update({m.group(1): m.group(2)})
    return model


def make_classes(model: str = SPDX_MODEL, out: str = OUTDIR) -> None:
    # get model latest commit date
    m = re.match(r'^(.*/spdx/spdx-3-model)/contents/(.+?)\s*$', SPDX_MODEL)
    q = f'{m.group(1)}/commits?path={m.group(2)}'
    commit = json.load(TextIOWrapper(urlopen(Request(q, headers=AUTH)), encoding='utf8'))[0]
    out += '_' + commit['commit']['committer']['date'].replace(':', '').replace('-', '')
    os.makedirs(out, exist_ok=True)

    model_refs = {}
    model_types = {
        '_commit': {
            'url': commit['url'],
            'html_url': commit['html_url'],
            'date': commit['commit']['committer']['date']},
        '_defaults': {}}
    e1 = list_dir(model)
    assert len(e1['files']) == 0
    for d1 in e1['dirs']:
        print(f'\n{d1.name}', end='')
        e2 = list_dir(d1.path)
        assert len(e2['files']) == 1
        model_types['_defaults'][d1.name] = load_model(open_file(e2['files'][0]))
        for d2 in e2['dirs']:
            # print(f'. {d2.name}')
            e3 = list_dir(d2.path)
            assert len(e3['dirs']) == 0
            assert d2.name in {'Classes', 'Datatypes', 'Vocabularies', 'Properties', 'Individuals'}
            if d2.name in {'Classes', 'Datatypes', 'Vocabularies'}:
                for f3 in e3['files']:
                    if not f3.name.startswith('_'):
                        print('.', end='')
                        model = load_model(open_file(f3))
                        meta = model['Metadata']
                        if meta['name'] in model_refs:
                            m = model_types[meta['name']]['Metadata']
                            print(f"###### Duplicate: {meta['name']} in {m['_profile']}/{m['_file']}, {d1.name}/{f3.name}")
                        ref = '/'.join((model_types['_defaults'][d1.name]['Metadata']['id'], meta['name']))
                        model_refs[meta['name']] = ref
                        meta['_modelRef'] = ref
                        meta['_profile'] = d1.name
                        meta['_category'] = d2.name
                        meta['_file'] = f3.name
                        meta['_html'] = f3.html
                        model_types[meta['name']] = model
                    else:
                        print('###### Ignored:', f3.name)

    print(f'\n{len(model_types) - 2} Types in model')
    with open(os.path.join(out, 'modelTypes.json'), 'w') as fp:
        json.dump(model_types, fp, indent=2)


if __name__ == '__main__':
    AUTH = {'Authorization': f'token {os.environ["GitHubToken"]}'}
    print(f'GitHub Token: ..{AUTH["Authorization"][-4:]}')
    fire.Fire(make_classes)
