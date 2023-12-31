# Python Implementations of SPDX-3.0 generation

These examples are meant to illustrate how tools may create SPDX 3.0 documents and how they may interact with each other. The examples follows the toy scenario below:
![image](simple_app.png)

This implementation only focuses on the acme application and the authors of the application.

## Documents

- `simple.py` is used to produce the `simple_acme.json` file. It requires Python3.10 and jq to run. In your environment, run `python simple.py | jq | tee <output_file_name>.json` to get the example content. This implementation faithfully reproduces the `CreationInfo` for all serialized elements. 
- `simple_compact.py` is used to produce `simple_compact_acme.json`. The usage is the same as the above. Here, the `CreationInfo` is applied only at the document level. This assumes the `CreationInfo` applies to all elements unless the elements themselves have a `creationInfo` blob.
- `compact_to_expand.py` converts the "simple compact" form into the expanded form. To use this script, run `python compact_to_expand.py < simple_compact_acme.json | jq | tee <output_file_name>.json. `compact_to_expand.json` is the result of using this script to convert the `simple_compact_acme.json` file into something similar to `simple_acme.json`.

## Notes
- Although we can implement the conversion from compacted to simple, the lack of information on the type of concrete class each of the elements are representing makes the internal model inaccurate.
