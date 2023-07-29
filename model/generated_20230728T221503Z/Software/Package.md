## [Package](https://github.com/spdx/spdx-3-model/blob/main/model/Software/Classes/Package.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class Package(/Software/SoftwareArtifact):
    packageVersion: String = None                      # * optional 
    downloadLocation: AnyUri = None                    # * optional 
    packageUrl: AnyUri = None                          # * optional 
    homePage: AnyUri = None                            # * optional 
    sourceInfo: String = None                          # * optional 
    contentIdentifier: AnyUri = None                   # * optional 
    primaryPurpose: SoftwarePurpose = None             # optional 
    additionalPurpose: SoftwarePurpose = None          # optional Set[1..*]
    concludedLicense: SpdxId = None                    # optional 
    declaredLicense: SpdxId = None                     # optional 
    copyrightText: String = None                       # * optional 
    attributionText: String = None                     # * optional 
    originatedBy: SpdxId = None                        # optional Set[1..*]
    suppliedBy: SpdxId = None                          # optional Set[1..*]
    builtTime: DateTime = None                         # optional 
    releaseTime: DateTime = None                       # optional 
    validUntilTime: DateTime = None                    # optional 
    standard: String = None                            # * optional Set[1..*]
    spdxId: SpdxId = None                              # 
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
