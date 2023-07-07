## [Package](https://github.com/spdx/spdx-3-model/blob/main/model/Software/Classes/Package.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class Package:
    packageVersion: String = None                      # optional 
    downloadLocation: AnyURI = None                    # optional 
    packageUrl: AnyURI = None                          # optional 
    homePage: AnyURI = None                            # optional 
    sourceInfo: String = None                          # optional 
    contentIdentifier: AnyURI = None                   # optional 
    primaryPurpose: SoftwarePurpose = None             # optional 
    additionalPurpose: SoftwarePurpose = None          # optional Set[1..*]
    concludedLicense: SpdxId = None                    # * optional 
    declaredLicense: SpdxId = None                     # * optional 
    copyrightText: String = None                       # optional 
    attributionText: String = None                     # optional 
    originatedBy: SpdxId = None                        # * optional Set[1..*]
    suppliedBy: SpdxId = None                          # * optional Set[1..*]
    builtTime: DateTime = None                         # optional 
    releaseTime: DateTime = None                       # optional 
    validUntilTime: DateTime = None                    # optional 
    standard: String = None                            # optional Set[1..*]
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
    namespaces: NamespaceMap = None                    # optional Set[1..*]
    imports: ExternalMap = None                        # optional Set[1..*]
```
