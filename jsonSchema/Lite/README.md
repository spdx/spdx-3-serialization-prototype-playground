# README for JSON Schema of Lite profile  

## What is this?  

This is a JSON schema file that meets Lite Profile.  
Lite Profile is a profile that specifies the minimum elements required for an actual OSS license compliance workflow.  
Lite profiles can also be combined with other profiles to meet requirements such as NTIA minimum elements.  
For more information on the purpose and usage of the Lite profile, please visit the following website: https://spdx.dev/learn/areas-of-interest/lite/  

## DISCUSSIONS / TODO  

- Agent class definition  
  The Agent class here is described as a concrete class that represents all of Person, Organization and SoftwareAgent.  
  and this JSON Schema lists only the minimum elements as a Lite Profile.  
  - spdxId, name, externalIdentifier  

- AnyLicenseInfo class definition  
  According to the SPDX 3.0 specification, the LicenseExpression and SimpleLicensingText classes seems to be associated by using  DictionaryEntry or Relationship classes.  
  But the AnyLicenseInfo class here is described as a concrete class that is merged LicenseExpression and SimpleLicensingText classes.  

- specVersion in CreationInfo  
  specVersion is a required element in the SPDX 3.0 specification. However, it may not be required in cases such as Relationship class objects.  

- Sbom and SpdxDocument class  
  The specification would list the Sbom class object as one of the elements of the SpdxDocument class object, but in this JSON schema it is a Schema up to the Sbom class.  

- downloadlocation and packageUrl in Package class  
  In a directory named visualized, there are configuration and png files to visualize the JSON schema using [PlantUML](https://plantuml.com/). Required elements are highlighted in lightgreen and **conditional required elements are highlighted in orange**.  

- TODO: adding other profiles  
  There is no other profile associated with this JSON schema.  
  We will add how the Lite profile should be described to associate with the other profiles such as Security profile.  

## EOF  
