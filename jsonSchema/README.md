# README  

## What is this?  

These json files are JSON schema for SPDX 3.0, correspond to spdx-3-model repo's commit id ["ca9738bd0fa0f826f9cccac76ca18e326af84d35" on Feb 18, 2024](https://github.com/spdx/spdx-3-model/commit/ca9738bd0fa0f826f9cccac76ca18e326af84d35).  
Currently, we have created JSON schemas for the following 3 profiles:  
 - Core  
 - SimpleLicensing  
 - Software  

And the Lite directory contains a JSON schema that focus on the classes and elements required for the Lite profile.  

## Directory tree structure  

Shemas are separated in each profile.  
```
JSON_Schema  
 |
 + - Core
 |    + - Json schema files (.json)
 |    + - visualized
 |         + - platuml files (.pu) for visualization
 |         + - visualized images
 + - Lite
     ... (snip, same as Core directory)
 + - SimpleLicensing
     ... (snip, same as Core directory)
 + - Software
     ... (snip, same as Core directory)
```

In a directory named visualized, there are configuration and png files to visualize the JSON schema using [PlantUML](https://plantuml.com/). Required elements are highlighted in lightgreen and conditional required elements are highlighted in orange.  
png files are created as follows:  

```
$ cd /path/to/visualized  
$ java -jar /path/to/plantuml.jar "*.pu"
```
ref: https://plantuml.com/en/command-line

# EOF  
