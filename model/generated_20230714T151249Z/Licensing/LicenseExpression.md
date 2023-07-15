## [LicenseExpression](https://github.com/spdx/spdx-3-model/blob/main/model/Licensing/Classes/LicenseExpression.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
```
class LicenseExpression(AnyLicenseInfo):
    licenseExpression: String = None                   # * 
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
