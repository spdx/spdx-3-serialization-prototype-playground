## [CreationInfo](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/CreationInfo.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class CreationInfo:
    specVersion: SemVer = None                         # optional Set[1..*]
    comment: String = None                             # * optional 
    created: DateTime = None                           # optional Set[1..*]
    createdBy: SpdxId = None                           # * Set[1..*]
    createdUsing: SpdxId = None                        # * optional Set[1..*]
    profile: ProfileIdentifierType = None              # Set[1..*]
    dataLicense: String = None                         # * optional Set[1..*]
```
