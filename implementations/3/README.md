# Python implementations for SPDX3.0 document generation: JSON alternative 3

This implementation takes the `simple_compact.py` script in implementation 1 and modifys it such that the concrete subclass is identified in the JSON serialization.

## Documents

`simple_compact.py` is used to generate `simple_compact_acme.json` as follows:
```
python simple_compact.py | jq | tee simple_compact_acme.json
```
Note that the timestamp may be different when you run it.

This implementation follows the same implementation of compaction from implementation 1, but the JSON is crafted in this form:

```
elements = {"person": [{"spdxId": ...}, {...},...],
            "organization": [...],
            ...}
```
Here, the elements is an object, not a list. The object contains a key for each kind of concrete class represented in the internal model. 

`compact_to_expand.py` reads `simple_compact_acme.json` and produces `simple_expand_acme.json` in this way:

```
python compact_to_expand.py < simple_compact_acme.json | jq | tee simple_expand_acme.json
```

In `simple_expand_acme.json`, `creationInfo` is included in each of the elements.

## Notes

Although we can identify the concrete classes in the JSON serialization, it still requires some implementation to find out which class to instantiate. In this way, this implementation isn't much different from the serialization where "type" is used as a key to indicate what concrete class to instantiate.
