# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass, fields
from generated.Core import CreationInfo, Element, Extension, ExternalIdentifier, ExternalMap, ExternalReference
from generated.Core import IntegrityMethod, NamespaceMap
from generated.Software import SBOMType


@dataclass
class Sbom:
    sbomType: SBOMType = None
    context: str = None
    element: Element = None
    rootElement: Element = None
    namespaces: NamespaceMap = None
    imports: ExternalMap = None
    spdxId: str = None
    name: str = None
    summary: str = None
    description: str = None
    comment: str = None
    creationInfo: CreationInfo = None
    verifiedUsing: IntegrityMethod = None
    externalReference: ExternalReference = None
    externalIdentifier: ExternalIdentifier = None
    extension: Extension = None


if __name__ == '__main__':
    sb = Sbom
    sb.sbomType = 'source'
    for f in fields(sb):
        print(f.name, f.type)
