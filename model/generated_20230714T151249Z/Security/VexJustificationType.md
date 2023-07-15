## [VexJustificationType](https://github.com/spdx/spdx-3-model/blob/main/model/Security/Vocabularies/VexJustificationType.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
```
class VexJustificationType(Enum):
    componentNotPresent = 1
    vulnerableCodeNotPresent = 2
    vulnerableCodeCannotBeControlledByAdversary = 3
    vulnerableCodeNotInExecutePath = 4
    inlineMitigationsAlreadyExist = 5
```
