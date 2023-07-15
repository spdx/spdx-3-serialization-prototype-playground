## [ExternalIdentifier](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalIdentifier.md)
Model: [7d135f6](https://github.com/spdx/spdx-3-model/commit/7d135f6b3c1c412e06ae2ca73da3cbbbcdbc5cda) 2023-07-14T15:12:49Z
```
class ExternalIdentifier():
    externalIdentifierType: ExternalIdentifierType = None # 
    identifier: String = None                          # * 
    comment: String = None                             # * optional 
    identifierLocator: String = None                   # * optional Set[1..*]
    issuingAuthority: String = None                    # * optional 
```
