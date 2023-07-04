# Individual Element Examples

The model directory contains Python example templates generated from the
[SPDX model]() files, along with the code to generate those templates.
## Model Types
* `parse_model.py` reads the model files from GitHub and writes a local snapshot file `model_types.json`
in the output directory, by default called `generated`.
* `make_types.py` reads the model snapshot and generates a Python class file for each type defined in the model.
These Python files are templates used to create logical examples of each type.

## Individual Element Examples
To create a new logical example, copy the type template (e.g. `person.py` into the [ex](../ex) folder,
give it an example name (e.g., `person1.py`) and fill in each of the property values
for that example.
