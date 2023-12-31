# spdx-3-serialization-prototype-playground
TEMPORARY repo to contain different draft examples for SPDX 3.0 serializations.

This repository is an open playground to experiment with different serialization formats and approaches for the SPDX 3.0 spec.

Once we have decided on the officially supported SPDX serializations, they will be documented in other repositories and this repository will be deleted.

## Directory Structure
Each serialization approach will be in a separate sub-directory.
The sub-directory will contain a README.md file with background on the serialization approach, a description on the different examples, and a link to any tools that can parse these files.

## Contributing
All contributions are licensed under CC0 - please sign-off any commits.

New serialization approaches should be in their own directories with an appropriate README.md file.

We will do a minimum review of new proposals before merging.

Suggestions to existing serialization approaches will be reviewed by the contributors of the original serializations approach before merging.

## Operating Principles
1. The [logical model](https://github.com/spdx/spdx-3-model/tree/main/model) is the single authoritative source for SPDXv3 content.
All examples submitted to the playground should correspond to the given model examples to allow for easy comparison.
The initial set of examples is from the SPDX v3 [serialization README](https://github.com/spdx/spdx-3-model/blob/main/serialization/README.md)
   (see [use cases](use_cases.md)).
2. The contributor for each serialization method is responsible for creating the examples and test code for that method.
3. The barrier to entry should be minimal. A contributor may create as many or as few examples as they deem appropriate for defining the method.
4. Although examples may be initially submitted to illustrate ideas before code has been developed to process them, serializing and parsing
code will eventually be necessary to demonstrate that the examples correctly reflect the model.

See [USING](model/USING.md) for more detail on the creation and use of model templates, logical examples, and serialized examples.

## Individual Element Examples
* The code for each serialization method translates between the logical examples and the corresponding serialized examples in both directions,
demonstrating the ability of the serialization method to correctly implement the model. This enables translation of serialized data from
any format to any other by reading and writing logical values.

| Logical Examples                                                | [RDF](rdf/README.md) | [XML](xml/README.md) | [JSON-LD](jsonld/README.md) |        [JSON1](json1/README.md)        |        [JSON2](json2/README.md)         | [JSON3](json3/README.md) | Protobuf | CBOR | YAML | [Text1](text1/README.md) |
|-----------------------------------------------------------------|:--------------------:|----------------------|-----------------------------|:--------------------------------------:|:---------------------------------------:|--------------------------|----------|:----:|------|:------------------------:|
| --- **Agents** ---                                              |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Agent1](ex/agent.md)                                           |                      |                      |                             |    [o](json1/examples/agent1.json)     |     [o](json2/examples/agent1.json)     |                          |          |      |      |                          |
| [Person1](ex/person1.md) with minimal CreationInfo              |                      |                      |                             |    [o](json1/examples/person1.json)    |    [o](json2/examples/person1.json)     |                          |          |      |      |                          |
| [Person2](ex/person2.md) with full CreationInfo                 |                      |                      |                             |    [o](json1/examples/person2.json)    |    [o](json2/examples/person2.json)     |                          |          |      |      |                          |
| [Person3](ex/person3.md) with no CreationInfo???                |                      |                      |                             |    [o](json1/examples/person3.json)    |    [o](json2/examples/person3.json)     |                          |          |      |      |                          |
| [Organization1](ex/organization1.md)                            |                      |                      |                             |     [o](json1/examples/org1.json)      |      [o](json2/examples/org1.json)      |                          |          |      |      |                          |
| [Tool1](ex/tool1.md) not an Agent                               |                      |                      |                             |     [o](json2/examples/tool1.json)     |     [o](json2/examples/tool1.json)      |                          |          |      |      |                          |
| --- **Annotations** ---                                         |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Annotation1](ex/annotation1.md)                                |                      |                      |                             |  [o](json1/examples/annotation1.json)  |  [o](json2/examples/annotation1.json)   |                          |          |      |      |                          |
| --- **Artifacts** ---                                           |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Package1](ex/package1.md)                                      |                      |                      |                             |   [o](json1/examples/package1.json)    |    [o](json2/examples/package1.json)    |                          |          |      |      |                          |
| [Package2](ex/package2.md) with ExternalIdentifier              |                      |                      |                             |   [o](json1/examples/package2.json)    |                                         |                          |          |      |      |                          |
| [Package3](ex/package3.md) with ExternalReference               |                      |                      |                             |   [o](json1/examples/package3.json)    |                                         |                          |          |      |      |                          |
| [File1](ex/file1.md)                                            |                      |                      |                             |     [o](json1/examples/file1.json)     |     [o](json2/examples/file1.json)      |                          |          |      |      |                          |
| [File2](ex/file2.md)                                            |                      |                      |                             |     [o](json1/examples/file2.json)     |     [o](json2/examples/file2.json)      |                          |          |      |      |                          |
| [Snippet1](ex/snippet1.md)                                      |                      |                      |                             |   [o](json1/examples/snippet1.json)    |                                         |                          |          |      |      |                          |
| --- **Relationships** ---                                       |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Relationship1](ex/relationship1.md) Pkg1, File1, File2         |                      |                      |                             | [o](json1/examples/relationship1.json) |                                         |                          |          |      |      |                          |
| [Relationship2](ex/relationship2.md) with time properties       |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [LifecycleScopeRelationship1](ex/lcsrelationship1.md)           |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [AssessmentRelationship1](ex/assessmentrelationship1.md)        |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SoftwareDependencyRelationship1](ex/swdeprelationshpi.md)      |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| --- **Collections** ---                                         |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Bom2](ex/bom1.md)                                              |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Sbom1](ex/sbom1.md) with two Files                             |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Sbom2](ex/sbom2.md) with Pkg1, File1, File2, Rel1              |                      |                      |                             |                                        |     [o](json2/examples/sbom1.json)      |                          |          |      |      |                          |                           |                      |                      |                             |                                        |     [o](json2/examples/sbom1.json)      |                          |          |      |      |                          |
| [Bundle1](ex/bundle1.md)                                        |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Bundle2](ex/bundle2.md) of Person1, Person2                    |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| --- **SpdxDocuments** ---                                       |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SpdxDocument1](ex/spdxdocument1.md) with two Files             |                      |                      |                             |                                        | [o](json2/examples/spdx_document1.json) |                          |          |      |      |                          |
| [SpdxDocument2](ex/spdxdocument2.md) with two Sboms             |                      |                      |                             |                                        | [o](json2/examples/spdx_document2.json) |                          |          |      |      |                          |
| [SpdxDocument3](ex/spdxdocument3.md) with NamespaceMap          |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SpdxDocument4](ex/spdxdocument4.md) with ExternalMap           |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SpdxDocument5](ex/spdxdocument5.md) v2.3 example               |                      |                      |                             |                                        | [o](json2/examples/spdx_document3.json) |                          |          |      |      |                          |
| --- **Licensing** ---                                           |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [License1](ex/license1.md) single artifact                      |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [CustomLicense1](ex/customlicense1.md) single artifact          |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [LicenseExpression1](ex/licenseexpression1.md) single artifact  |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [LicenseExpression2](ex/licenseexpression2.md) single artifact  |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [LicenseExpression3](ex/licenseexpression3.md) two artifacts    |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| --- **Security** ---                                            |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
|                                                                 |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| --- **Build** ---                                               |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
|                                                                 |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |

*NOTE: need list of element types required by each licensing use case, specify which artifact examples*

## Multiple Element Examples
* An element set is the list of individual element example values that are included in a Payload.  
* A Payload is the result of combining the element set into serialized data in a method-specific manner.
* The code for a method translates between the Payload and its element set in both directions. 

| Example                 | [RDF](rdf/README.md) | [XML](xml/README.md) | [JSON-LD](jsonld/README.md) |       [JSON1](json_ld/README.md)       |        [JSON2](json1/README.md)        | [JSON3](json2/README.md) | Protobuf | CBOR | YAML | [Text1](text1/README.md) |
|-------------------------|:--------------------:|----------------------|-----------------------------|:--------------------------------------:|:--------------------------------------:|--------------------------|----------|:----:|------|:------------------------:|
| Payload1 - File1, File2 |                      |                      |                             |                                        | [o](json2/examples/spdx_payload1.json) |                          |          |      |      |                          |
| Payload2 - Sbom1, Sbom2 |                      |                      |                             |                                        | [o](json2/examples/spdx_payload2.json) |                          |          |      |      |                          |
| Payload3 - v2.3         |                      |                      |                             | [o](json1/examples/spdx_payload3.json) |                                        |                          |          |      |      |                          |

