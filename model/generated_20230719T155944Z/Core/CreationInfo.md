## [CreationInfo](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/CreationInfo.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class CreationInfo():
    specVersion: SemVer = None                         # 
    comment: String = None                             # * optional 
    created: DateTime = None                           # optional 
    createdBy: SpdxId = None                           # * Set[1..*]
    createdUsing: SpdxId = None                        # * optional Set[1..*]
    profile: ProfileIdentifierType = None              # Set[1..*]
    dataLicense: String = None                         # * optional 
```
