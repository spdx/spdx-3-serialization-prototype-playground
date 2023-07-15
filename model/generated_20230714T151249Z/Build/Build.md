## [Build](https://github.com/spdx/spdx-3-model/blob/main/model/Build/Classes/Build.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
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
