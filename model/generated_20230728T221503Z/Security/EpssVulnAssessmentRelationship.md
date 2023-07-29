## [EpssVulnAssessmentRelationship](https://github.com/spdx/spdx-3-model/blob/main/model/Security/Classes/EpssVulnAssessmentRelationship.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    probability: xsd:nonNegativeInteger = None         # 
    severity: String = None                            # * optional 
    assessedElement: SpdxId = None                     # optional 
    publishedTime: DateTime = None                     # optional 
    suppliedBy: SpdxId = None                          # optional 
    modifiedTime: DateTime = None                      # optional 
    withdrawnTime: DateTime = None                     # optional 
    from: SpdxId = None                                # 
    to: SpdxId = None                                  # optional Set[1..*]
    relationshipType: RelationshipType = None          # 
    completeness: RelationshipCompleteness = None      # optional 
    startTime: DateTime = None                         # optional 
    endTime: DateTime = None                           # optional 
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
