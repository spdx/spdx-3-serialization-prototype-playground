# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass, fields
from model import String
from generated.Core import CreationInfo, Extension, ExternalIdentifier, ExternalMap, ExternalReference
from generated.Core import IntegrityMethod, NamespaceMap, SpdxId
from generated.Software import SbomType


@dataclass
class Sbom:
    sbomType: SbomType = None                          # optional Set[1..*]
    context: String = None                             # optional
    element: SpdxId = None                             # * Set[1..*]
    rootElement: SpdxId = None                         # * Set[1..*]
    namespaces: NamespaceMap = None                    # optional Set[1..*]
    imports: ExternalMap = None                        # optional Set[1..*]
    spdxId: SpdxId = None                              # *
    name: String = None                                # optional
    summary: String = None                             # optional
    description: String = None                         # optional
    comment: String = None                             # optional
    creationInfo: CreationInfo = None                  #
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    externalReference: ExternalReference = None        # optional Set[1..*]
    externalIdentifier: ExternalIdentifier = None      # optional Set[1..*]
    extension: Extension = None                        # optional Set[1..*]


# TODO: Generate setters for typing validation
# TODO: Create test fixtures for use case examples
if __name__ == '__main__':
    sb = Sbom(**{
        'sbomType': 'source',
        'element': 'foo',
        'spdxId': 'foo',
        'creationInfo': {
            'specVersion': '3.0.0',
            'profile': ['Core', 'Software']
        }
    })
    for f in fields(sb):
        print(f.name, f.type)

    print(sb)
