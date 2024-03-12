# Native JSON-LD Serialization

This is the JSON-LD examples and code bindings as currently discussed in the
SPDX Tech call

The JSON-LD format used by SPDX is complete JSON-LD implementation, however it
is restricted to a strict subset of full JSON-LD. This subset is enforces by a
JSON schema file. Doing the format in this way allows the files to be parsed by
either a full JSON-LD/RDF library for complex manipulations, or by simpler JSON
parsers if they do not need the full IRIs/etc, thereby increasing the ability
to exchange documents between parties and decrease the barrier to entry for
people writing tools to deal with SPDX documents (over multiple formats).

The generated JSON schema is carefully chosen to keep documents as easy to
write by hand as possible, with the goal that the same document format can be
used for both the "simple" SPDX uses cases, as well as the more complex ones.

All generated code bindings and JSON schema files are generated using
[shacl2code](https://github.com/JPEWdev/shacl2code).

## JSON Schema Validation

An SPDX document can be validated against the JSON Schema by referencing the
schema provided at the URL
https://raw.githubusercontent.com/spdx/spdx-3-serialization-prototype-playground/main/jsonld/spdx-3.0-schema.json
For example, to use the Python `check-jsonschema` package, use:
```shell
check-jsonschema \
    -v --traceback-mode full \
    --schemafile https://raw.githubusercontent.com/spdx/spdx-3-serialization-prototype-playground/main/jsonld/spdx-3.0-schema.json \
    <FILE_TO_CHECK>
```

In general, the JSON schema is fairly complete in it's structural evaluation of
JSON-LD documents. However, it should be noted that it is not possible for it
to do a complete semantic evaluation of a document using JSON Schema. For that,
the document shoule be validated against the SHACL ontology.

Put another way, the JSON Schema can ensure that the document is parseable by
an compliant SPDX parser, but it cannot ensure that the contents of said
document make sense.


## SHACL Validation

The semantics of an SPDX document can be validated using the SHACL ontology
provided at the URL:
https://raw.githubusercontent.com/spdx/spdx-3-serialization-prototype-playground/main/jsonld/spdx-3.0-ontology.rdf.ttl

Note that this document is _both_ the ontology and shapes graph

For example, to validate using python `pyshacl`, use:
```shell
pyshacl -f human \
    --shacl https://raw.githubusercontent.com/spdx/spdx-3-serialization-prototype-playground/main/jsonld/spdx-3.0-ontology.rdf.ttl \
    --ont-graph https://raw.githubusercontent.com/spdx/spdx-3-serialization-prototype-playground/main/jsonld/spdx-3.0-ontology.rdf.ttl \
    -df json-ld \
    <FILE_TO_CHECK>
```


## Generated Bindings

Various generated language bindings can be found in the `bindings` directory.
For the present, these can be copied into your codebase to be used.

## Examples

The Examples in the `examples` directory have all been validated against the
provided JSON schema and SHACL model


## TODOs
1. The examples in the `compactification_examples` directory are not updated to
   match the JSON schema yet
