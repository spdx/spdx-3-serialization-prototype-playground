## [AIPackage](https://github.com/spdx/spdx-3-model/blob/main/model/AI/Classes/AIPackage.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class AIPackage:
    energyConsumption: str = None                      # optional 
    standardCompliance: str = None                     # optional Set[1..*]
    limitation: str = None                             # optional 
    typeOfModel: str = None                            # optional Set[1..*]
    informationAboutTraining: str = None               # optional 
    informationAboutApplication: str = None            # optional 
    hyperparameter: /Core/DictionaryEntry = None       # optional Set[1..*]
    modelDataPreprocessing: str = None                 # optional Set[1..*]
    modelExplainability: str = None                    # optional Set[1..*]
    sensitivePersonalInformation: PresenceType = None  # optional 
    metricDecisionThreshold: /Core/DictionaryEntry = None # optional Set[1..*]
    metric: /Core/DictionaryEntry = None               # optional Set[1..*]
    domain: str = None                                 # optional Set[1..*]
    autonomyType: PresenceType = None                  # optional 
    safetyRiskAssessment: SafetyRiskAssessmentType = None # optional 
    packageVersion: str = None                         # optional 
    downloadLocation: AnyUri = None                    # * optional 
    packageUrl: AnyUri = None                          # * optional 
    homePage: AnyUri = None                            # * optional 
    sourceInfo: str = None                             # optional 
    contentIdentifier: AnyUri = None                   # * optional 
    primaryPurpose: SoftwarePurpose = None             # optional 
    additionalPurpose: SoftwarePurpose = None          # optional Set[1..*]
    concludedLicense: /Licensing/AnyLicenseInfo = None # optional 
    declaredLicense: /Licensing/AnyLicenseInfo = None  # optional 
    copyrightText: str = None                          # optional 
    attributionText: str = None                        # optional 
    originatedBy: SpdxId = None                        # * optional Set[1..*]
    suppliedBy: SpdxId = None                          # * optional Set[1..*]
    builtTime: DateTime = None                         # optional 
    releaseTime: DateTime = None                       # optional 
    validUntilTime: DateTime = None                    # optional 
    standard: str = None                               # optional Set[1..*]
    spdxId: SpdxId = None                              # * 
    name: str = None                                   # optional 
    summary: str = None                                # optional 
    description: str = None                            # optional 
    comment: str = None                                # optional 
    creationInfo: CreationInfo = None                  # 
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    externalReference: ExternalReference = None        # optional Set[1..*]
    externalIdentifier: ExternalIdentifier = None      # optional Set[1..*]
    extension: Extension = None                        # optional Set[1..*]
    namespaces: NamespaceMap = None                    # optional Set[1..*]
    imports: ExternalMap = None                        # optional Set[1..*]
```
