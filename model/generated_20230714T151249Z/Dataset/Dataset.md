## [Dataset](https://github.com/spdx/spdx-3-model/blob/main/model/Dataset/Classes/Dataset.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
```
class Dataset(/Software/Package):
    datasetType: DatasetType = None                    # Set[1..*]
    dataCollectionProcess: String = None               # * optional 
    intendedUse: String = None                         # * optional 
    datasetSize: xsd:nonNegativeInteger = None         # optional 
    datasetNoise: String = None                        # * optional 
    dataPreprocessing: String = None                   # * optional Set[1..*]
    sensor: DictionaryEntry = None                     # optional Set[1..*]
    knownBias: String = None                           # * optional Set[1..*]
    sensitivePersonalInformation: PresenceType = None  # optional 
    anonymizationMethodUsed: String = None             # * optional Set[1..*]
    confidentialityLevel: ConfidentialityLevelType = None # optional 
    datasetUpdateMechanism: String = None              # * optional 
    datasetAvailability: DatasetAvailabilityType = None # optional 
    packageVersion: String = None                      # * optional 
    downloadLocation: String = None                    # * optional 
    packageUrl: String = None                          # * optional 
    homePage: String = None                            # * optional 
    sourceInfo: String = None                          # * optional 
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
