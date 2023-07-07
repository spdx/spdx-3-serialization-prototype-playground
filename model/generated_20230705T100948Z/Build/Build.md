## [Build](https://github.com/spdx/spdx-3-model/blob/main/model/Build/Classes/Build.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class Build:
    buildType: AnyURI = None                           # 
    buildId: String = None                             # optional 
    configSourceEntrypoint: String = None              # optional Set[1..*]
    configSourceUri: AnyURI = None                     # optional Set[1..*]
    configSourceDigest: Hash = None                    # optional Set[1..*]
    parameters: DictionaryEntry = None                 # optional Set[1..*]
    buildStartTime: DateTime = None                    # optional 
    buildEndTime: DateTime = None                      # optional 
    environment: DictionaryEntry = None                # optional Set[1..*]
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
