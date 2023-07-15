## [CreationInfo](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/CreationInfo.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
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
