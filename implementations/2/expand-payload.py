import json
import os
from urllib.parse import urlparse

OUT = 'out'
SPDXID_PROPERTIES = ['spdxId']      # Add all properties of type Element from model


def expand_iri(iri: str, nsmap: dict) -> str:
    """
    Expand a prefixed IRI string ("foo" or "ns:foo") to a full IRI ("http://example.com/foo")
    """
    if urlparse(iri).scheme:    # do nothing if already an IRI
        return iri
    p = iri.split(':', maxsplit=1)
    return nsmap['' if len(p) < 2 else p[0]] + p[-1]


def expand_element(element: dict, nsmap: dict = {}, cimap: dict = {}) -> dict:
    """
    Expand a compact Payload Element to a full Element by updating SpdxIds and CreationInfo
    """
    e = dict(element)   # Make a copy that can be modified

    ci = e.get('creationInfo', '')  # Fill in compacted creation info
    e['creationInfo'] = cimap[ci] if isinstance(ci, str) else ci

    if nsmap:   # Validate format of namespaceMap
        assert '' in nsmap, 'namespaceMap has no default IRI'
        for k, v in nsmap.items():
            assert v[-1] in '/#', f'namespaceMap {k} has no separator: {v}'

        for p in SPDXID_PROPERTIES:     # Fill in compacted IRIs
            e[p] = expand_iri(e[p], nsmap)

    return e


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for file in os.scandir():
        if file.name.startswith('payload') and os.path.splitext(file.name)[1] == '.json':
            with open(file.name) as fp:
                p = json.load(fp)
            elements = [expand_element(e, p.get('namespaceMap', {}), p.get('creationInfoMap', {})) for e in p['element']]
            with open(os.path.join(OUT, file.name.replace('payload', 'elements')), 'w') as fp:
                json.dump(elements, fp, indent=2)