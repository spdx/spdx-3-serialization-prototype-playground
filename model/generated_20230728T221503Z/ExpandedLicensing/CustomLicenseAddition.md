## [CustomLicenseAddition](https://github.com/spdx/spdx-3-model/blob/main/model/ExpandedLicensing/Classes/CustomLicenseAddition.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class CustomLicenseAddition(LicenseAddition):
    additionText: String = None                        # * 
    standardAdditionTemplate: String = None            # * optional 
    isDeprecatedAdditionId: xsd:boolean = None         # optional 
    obsoletedBy: String = None                         # * optional 
    spdxId: SpdxId = None                              # 
    name: String = None                                # * 
    summary: String = None                             # * optional 
    description: String = None                         # * optional 
    comment: String = None                             # * optional 
    creationInfo: CreationInfo = None                  # 
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    externalReference: ExternalReference = None        # optional Set[1..*]
    externalIdentifier: ExternalIdentifier = None      # optional Set[1..*]
    extension: Extension = None                        # optional Set[1..*]
```
