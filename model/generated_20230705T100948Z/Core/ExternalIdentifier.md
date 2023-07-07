## [ExternalIdentifier](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalIdentifier.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class ExternalIdentifier:
    externalIdentifierType: ExternalIdentifierType = None # 
    identifier: String = None                          # 
    comment: String = None                             # optional 
    identifierLocator: AnyUri = None                   # * optional Set[1..*]
    issuingAuthority: AnyUri = None                    # * optional 
```