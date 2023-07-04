# Using the Serialization Playground

## Structure
The playground directory structure has three components:
1. A directory of Python [template classes](generated), with one template for each type defined by the model.
Each template lists just the properties of the type, with no property values.
2. A directory of Python [example classes](../ex) with property values from a template class filled in,
3. A directory of serialized examples for each proposed serialization format, e.g., [JSON1](../json1).

### Template Classes
The template classes are generated from the logical model:
```
class Sbom:
    sbomType: SBOMType = None
    context: str = None
    element: AnyUri = None
    rootElement: AnyUri = None
    namespaces: NamespaceMap = None
    imports: ExternalMap = None
    spdxId: AnyUri = None
    name: str = None
    summary: str = None
    description: str = None
    comment: str = None
    creationInfo: CreationInfo = None
    verifiedUsing: IntegrityMethod = None
    externalReference: ExternalReference = None
    externalIdentifier: ExternalIdentifier = None
    extension: Extension = None
```

### Example Logical Values
One example for each of the use cases listed in the [README](README.md).
Each example logical value is a copy of the template for that type with property values filled in.
Many of the model types will not have a use case, and a few types will have several use cases / examples.
Contributors may propose additional example logical values to accompany corresponding serialized data.

These are the logical values to be serialized into various serialization formats.
All required properties must have a value; optional properties may be left empty (Python None).
```
class Sbom:
    sbomType: SBOMType = 'source'
    context: str = None
    ... TBSL ...
```
### Serialized Examples
The contributor of a format shows how an example logical value is serialized and parsed
to/from the serialized value for that use case.