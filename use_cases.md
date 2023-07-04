# Serialization Use Cases
Mapping from spdx-3-model [use case list](https://github.com/spdx/spdx-3-model/blob/main/serialization/README.md)
to Element Examples

- **Person:** [Person1](ex/person1.md) with minimal CreationInfo 
- **Agent:** [Agent1](ex/agent.md)
- **Annotation:** [Annotation1](ex/annotation1.md)
- **File:** [File1](ex/file1.md)
- **Package:** [Package1](ex/package1.md) with [File1](ex/file1.md) and [File2](ex/file2.md)
- **Package:** [Package2](ex/package2.md) with ExternalIdentifier
- **Package:** [Package3](ex/package3.md) with ExternalReference
- **Relationship:** [Relationship1](ex/relationship1.md) with [Package1](ex/package1.md) contains two Files
- **Relationship:** [Relationship2](ex/relationship2.md) with time properties
- **SBOM:** [Sbom1](ex/sbom1.md) with two Files
- **SpdxDocument:** [SpdxDocument1](ex/spdxdocument1.md) with two Files
- **SpdxDocument:** [SpdxDocument3](ex/spdxdocument3.md) with NamespaceMap
- **SpdxDocument:** [SpdxDocument4](ex/spdxdocument4.md) with ExternalMap
- **Person:** [Person3](ex/person3.md) with no CreationInfo *NOTE: invalid after model update*
- **Person:** [Person1](ex/person1.md) with minimal CreationInfo
- **Person:** [Person2](ex/person2.md) with full CreationInfo
- **Bundle:** [Bundle1](ex/bundle1.md) *Note: with no elements?*
- **two Persons:** [Person1](ex/person1.md) and [Person2](ex/person2.md)
- **Bundle:** [Bundle2](ex/bundle2.md) of [Person1](ex/person1.md) and [Person2](ex/person2.md)

Licensing use cases:
- single artifact under one listed license: [License1](ex/license1.md)?
- single artifact under one custom license: [CustomLicense1](ex/customlicense1.md)?
- single artifact under license expression of listed licenses: [LicenseExpression1](ex/licenseexpression1.md)?
- single artifact under license expression of listed and custom licenses: [LicenseExpression2](ex/licenseexpression2.md)?
- two artifacts under same license expression of listed and custom licenses: [LicenseExpression3](ex/licenseexpression3.md)?

*NOTE: need list of element types required by each licensing use case, specify which artifact examples*

- security use cases to be added here
- build use cases to be added here