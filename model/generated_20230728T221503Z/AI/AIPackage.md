## [AIPackage](https://github.com/spdx/spdx-3-model/blob/main/model/AI/Classes/AIPackage.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class AIPackage(/Software/Package):
    energyConsumption: String = None                   # * optional 
    standardCompliance: String = None                  # * optional Set[1..*]
    limitation: String = None                          # * optional 
    typeOfModel: String = None                         # * optional Set[1..*]
    informationAboutTraining: String = None            # * optional 
    informationAboutApplication: String = None         # * optional 
    hyperparameter: DictionaryEntry = None             # optional Set[1..*]
    modelDataPreprocessing: String = None              # * optional Set[1..*]
    modelExplainability: String = None                 # * optional Set[1..*]
    sensitivePersonalInformation: PresenceType = None  # optional 
    metricDecisionThreshold: DictionaryEntry = None    # optional Set[1..*]
    metric: DictionaryEntry = None                     # optional Set[1..*]
    domain: String = None                              # * optional Set[1..*]
    autonomyType: PresenceType = None                  # optional 
    safetyRiskAssessment: SafetyRiskAssessmentType = None # optional 
    packageVersion: String = None                      # * 
    downloadLocation: AnyUri = None                    # * 
    packageUrl: AnyUri = None                          # * optional 
    homePage: AnyUri = None                            # * optional 
    sourceInfo: String = None                          # * optional 
    contentIdentifier: AnyUri = None                   # * optional 
    primaryPurpose: SoftwarePurpose = None             # 
    additionalPurpose: SoftwarePurpose = None          # optional Set[1..*]
    concludedLicense: SpdxId = None                    # optional 
    declaredLicense: SpdxId = None                     # optional 
    copyrightText: String = None                       # * optional 
    attributionText: String = None                     # * optional 
    originatedBy: SpdxId = None                        # optional Set[1..*]
    suppliedBy: SpdxId = None                          # Set[1..*]
    builtTime: DateTime = None                         # optional 
    releaseTime: DateTime = None                       # 
    validUntilTime: DateTime = None                    # optional 
    standard: String = None                            # * optional Set[1..*]
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
