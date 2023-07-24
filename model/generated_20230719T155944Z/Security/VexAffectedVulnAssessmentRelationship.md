## [VexAffectedVulnAssessmentRelationship](https://github.com/spdx/spdx-3-model/blob/main/model/Security/Classes/VexAffectedVulnAssessmentRelationship.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class VexAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    actionStatement: String = None                     # * optional 
    actionStatementTime: DateTime = None               # optional Set[1..*]
    vexVersion: String = None                          # * optional 
    statusNotes: String = None                         # * optional 
    assessedElement: SpdxId = None                     # * optional 
    publishedTime: DateTime = None                     # optional 
    suppliedBy: SpdxId = None                          # * optional 
    modifiedTime: DateTime = None                      # optional 
    withdrawnTime: DateTime = None                     # optional 
    from: SpdxId = None                                # * 
    to: SpdxId = None                                  # * optional Set[1..*]
    relationshipType: RelationshipType = None          # 
    completeness: RelationshipCompleteness = None      # optional 
    startTime: DateTime = None                         # optional 
    endTime: DateTime = None                           # optional 
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