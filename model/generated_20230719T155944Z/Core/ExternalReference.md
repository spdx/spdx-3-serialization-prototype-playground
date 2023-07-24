## [ExternalReference](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalReference.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class ExternalReference(none):
    externalReferenceType: ExternalReferenceType = None # optional 
    locator: AnyURI = None                             # optional Set[1..*]
    contentType: MediaType = None                      # optional 
    comment: String = None                             # * optional 
```
