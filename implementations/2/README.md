# JSON Serialization

This code applies optional namespaceMap and creationInfoMap to a compact JSON Payload:
```json
{
  "namespaceMap": {},
  "creationInfoMap": {},
  "element": [
    "element1",
    "element2",
    "..."
  ]
}
```
and returns a list of full elements:
```json
[
  "element1",
  "element2",
  "..."
]
```
If the Payload has no namespaceMap, no IRI expansion is performed.
If the Payload has no creationInfoMap, every Payload element must have CreationInfo.
Payload elements with full SpdxId and CreationInfo are returned unchanged.

## Usage
1. Create compacted .json files with filename beginning with "payload"
2. Run `expand-payload.py` to create corresponding "element" .json files in directory "out"