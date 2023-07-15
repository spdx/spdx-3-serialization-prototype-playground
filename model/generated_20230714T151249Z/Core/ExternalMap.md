## [ExternalMap](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalMap.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
```
class ExternalMap(none):
    externalId: String = None                          # * 
    verifiedUsing: IntegrityMethod = None              # optional Set[1..*]
    locationHint: String = None                        # * optional 
    definingDocument: String = None                    # * optional 
```
