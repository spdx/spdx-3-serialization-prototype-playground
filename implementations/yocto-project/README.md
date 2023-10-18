# YoctoProject/OpenEmbedded SPDX3 generation examples

This directory contains examples of serialization from the implementation (work in progress)
of the YoctoProject/OpenEmbedded SPDX3 generator. The generator code is contained in a separate
repository.

## Context

YoctoProject/OpenEmbedded is a project offering a system to create an operating system
(typically Linux) distribution. It is heavily used for embedded products.

The SPDX generation code is run during the build process, when we have access to all
source files and dependencies between them.

## Documents

`creationInfo-example-recipe-base-files.spdx.json` contains an example of generation for
a simple package with creationInfo.

`file-example-recipe-base-files.spdx.json` is adding listing of all files contained in
the package

`relationship-example-recipe-base-files.spdx.json` adds a simple relationship


## Notes

We have a number of questions about the approach. We are also going to combine multiple
files as in examples above to generate a complete SPDX of a system image.

## Open Questions

1. Is it possible to have several ElementCollection in one model ? Can we have collections inside collections ?
In other words, how many nodes of Element can there be in a branch of the tree ?

2. What objects should be at top level in the json ld output ? All Element ?

3. We need a complex example with complex relationships.

4. Do we have a chance to successful a json merge without full parsing and full
modelization ?

5. What should the serialization of suppliedBy be: an array or a single string?

6. In the profile Software, class : Package, attribute: homepage
Issue: the attribute is sometimes referred to as "homepage" and sometimes as "homePage"

