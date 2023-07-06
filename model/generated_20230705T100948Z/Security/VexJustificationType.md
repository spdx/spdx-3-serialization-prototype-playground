## [VexJustificationType](https://github.com/spdx/spdx-3-model/blob/main/model/Security/Vocabularies/VexJustificationType.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class VexJustificationType(Enum):
    componentNotPresent = 1
    vulnerableCodeNotPresent = 2
    vulnerableCodeCannotBeControlledByAdversary = 3
    vulnerableCodeNotInExecutePath = 4
    inlineMitigationsAlreadyExist = 5
```
