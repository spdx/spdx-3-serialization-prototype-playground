## [CreationInfo](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/CreationInfo.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class CreationInfo():
    specVersion: SemVer = None                         # 
    comment: String = None                             # * optional 
    created: DateTime = None                           # optional 
    createdBy: SpdxId = None                           # Set[1..*]
    createdUsing: SpdxId = None                        # optional Set[1..*]
    profile: ProfileIdentifierType = None              # Set[1..*]
    dataLicense: String = None                         # * optional 
```
