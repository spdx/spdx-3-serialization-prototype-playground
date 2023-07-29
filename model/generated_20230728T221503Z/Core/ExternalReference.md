## [ExternalReference](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalReference.md)
Model: [8dff2a3](https://github.com/spdx/spdx-3-model/commit/8dff2a3243c9e00e1eb170fac749450a845ccdd6) 2023-07-28T22:15:03Z
```
class ExternalReference(none):
    externalReferenceType: ExternalReferenceType = None # optional 
    locator: AnyUri = None                             # * optional Set[1..*]
    contentType: MediaType = None                      # optional 
    comment: String = None                             # * optional 
```
