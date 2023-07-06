## [LicenseAddition](https://github.com/spdx/spdx-3-model/blob/main/model/Licensing/Classes/LicenseAddition.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class LicenseAddition:
    additionText: str = None                           # 
    standardAdditionTemplate: str = None               # optional 
    isDeprecatedAdditionId: xsd:boolean = None         # optional 
    obsoletedBy: str = None                            # optional 
    spdxId: SpdxId = None                              # * 
    name: str = None                                   # optional 
    summary: str = None                                # optional 
    description: str = None                            # optional 
    comment: str = None                                # optional 
    creationInfo: CreationInfo = None                  # 
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    externalReference: ExternalReference = None        # optional Set[1..*]
    externalIdentifier: ExternalIdentifier = None      # optional Set[1..*]
    extension: Extension = None                        # optional Set[1..*]
    namespaces: NamespaceMap = None                    # optional Set[1..*]
    imports: ExternalMap = None                        # optional Set[1..*]
```
