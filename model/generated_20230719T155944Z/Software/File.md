## [File](https://github.com/spdx/spdx-3-model/blob/main/model/Software/Classes/File.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class File(/Software/SoftwareArtifact):
    contentType: MediaType = None                      # optional 
    contentIdentifier: String = None                   # * optional 
    primaryPurpose: SoftwarePurpose = None             # optional 
    additionalPurpose: SoftwarePurpose = None          # optional Set[1..*]
    concludedLicense: SpdxId = None                    # * optional 
    declaredLicense: SpdxId = None                     # * optional 
    copyrightText: String = None                       # * optional 
    attributionText: String = None                     # * optional 
    originatedBy: SpdxId = None                        # * optional Set[1..*]
    suppliedBy: SpdxId = None                          # * optional Set[1..*]
    builtTime: DateTime = None                         # optional 
    releaseTime: DateTime = None                       # optional 
    validUntilTime: DateTime = None                    # optional 
    standard: String = None                            # * optional Set[1..*]
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
