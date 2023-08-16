import hashlib
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model


def camel_case(string):
    # Utility function to convert snake_case to camelCase
    # Used to satisty conventions described in `model`
    words = string.split("_")
    camel = words[0].lower() + ''.join(word.lower().title() for word in words[1:])
    return camel


def mint(agents, profiles, program):
    # Create a CreationInfo object to be used throughout the document
    return model.CreationInfo(spec_version=Version('3.0.0'),
                              created=datetime.utcnow(),
                              created_by=agents,
                              profile=profiles,
                              created_using=[program])


def created_dict(cinfo):
    # converts a CreationInfo object into a dictionary
    profiles = []
    for pro in cinfo.profile:
        profiles.append(pro.name)
    return({"specVersion": f"{cinfo.spec_version.major}.{cinfo.spec_version.minor}.{cinfo.spec_version.patch}",
            "created": cinfo.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "createdBy": cinfo.created_by,
            "profile": profiles,
            "dataLicense": cinfo.data_license,
            "createdUsing": cinfo.created_using})

# The compact versions of these functions do not include the
# creation_info key


def person_dict(p):
    # converts a Person object into a dictionary
    return({"spdxId": p.spdx_id,
            "type": "Person"})


def org_dict(o):
    # converts an Organization object into a dictionary
    return({"spdxId": o.spdx_id,
            "type": "Organization"})


def app_dict(app):
    # converts a Package object into a dictionary
    return({"spdxId": app.spdx_id,
            "name": app.name,
            "packageVersion": app.package_version,
            "type": "Package"})


def doc_dict(doc):
    # converts a Document object into a dictionary
    return({"spdxId": doc.spdx_id,
            "name": doc.name,
            "element": doc.element,
            "rootElement": doc.root_element,
            "creationInfo": created_dict(doc.creation_info),
            "type": "SpdxDocument"})


def relationship_dict(rel):
    # converts a Relationship object into a dictionary
    return({"spdxId": rel.spdx_id,
            "fromElement": rel.from_element,
            "relationshipType": camel_case(rel.relationship_type.name),
            "to": rel.to})


def hash_dict(hashobj):
    # converts a Hash object into a dictionary
    return({"hashAlgorithm": hashobj.algorithm.name,
            "hashValue": hashobj.hash_value,
            "type": "Hash"})


def external_map_dict(extmap):
    # convert and ExternalMap object into a dictionary
    verified_using = []
    for vu in extmap.verified_using:
        verified_using.append(hash_dict(vu))
    return({"externalId": extmap.external_id,
            "verifiedUsing": verified_using,
            "locationHint": extmap.location_hint,
            "type": "ExternalMap"})


def make_elements(elements):
    # This implementation currently checks for just Person, Organization,
    # and Package but the logic should be the same for all concrete classes
    elblob = {"person": [],
              "organization": [],
              "package": []}
    for el in elements:
        # introspection may not be possible in some languages, in which
        # case, something needs to store the class name in the object itself
        if el.__class__.__name__ == "Person":
            elblob["person"].append(person_dict(el))
        if el.__class__.__name__ == "Organization":
            elblob["organization"].append(org_dict(el))
        if el.__class__.__name__ == "Package":
            elblob["package"].append(app_dict(el))
    return elblob


def get_integrity(filename):
    # Read a local file, calculate its hash and return an IntegrityMethod
    # object
    with open(filename, 'rb') as f:
        content = f.read()
    return model.Hash(model.HashAlgorithm.sha256,
                      hashlib.sha256(content).hexdigest())
