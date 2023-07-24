## [Build](https://github.com/spdx/spdx-3-model/blob/main/model/Build/Classes/Build.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class Build(/Core/Element):
    buildType: String = None                           # * 
    buildId: String = None                             # * optional 
    configSourceEntrypoint: String = None              # * optional Set[1..*]
    configSourceUri: String = None                     # * optional Set[1..*]
    configSourceDigest: Hash = None                    # optional Set[1..*]
    parameters: DictionaryEntry = None                 # optional Set[1..*]
    buildStartTime: DateTime = None                    # optional 
    buildEndTime: DateTime = None                      # optional 
    environment: DictionaryEntry = None                # optional Set[1..*]
    spdxId: SpdxId = None                              # * 
    name: String = None                                # * optional 
    summary: String = None                             # * optional 
    description: String = None                         # * optional 
    comment: String = None                             # * optional 
    creationInfo: CreationInfo = None                  # 
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    externalReference: ExternalReference = None        # optional Set[1..*]
    externalIdentifier: ExternalIdentifier = None      # optional Set[1..*]
    extension: Extension = None                        # optional Set[1..*]
```