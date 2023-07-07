## [ExternalReference](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalReference.md)
Model: [828388b](https://github.com/spdx/spdx-3-model/commit/828388b98c2374f1af6b760ab87fee0d4a11e3f4) 2023-07-05T10:09:48Z
```
class ExternalReference:
    externalReferenceType: ExternalReferenceType = None # optional 
    locator: AnyUri = None                             # * optional Set[1..*]
    contentType: MediaType = None                      # optional 
    comment: String = None                             # optional 
```
