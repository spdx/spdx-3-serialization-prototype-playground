import hashlib
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software


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


def dict_created(cblob):
    # converts a creationInfo dictionary into a CreationInfo object
    pl = []
    for profile in cblob["profile"]:
        pl.append(model.ProfileIdentifierType[profile])
    return model.CreationInfo(spec_version=Version(cblob["specVersion"]),
                              created=datetime.strptime(
                                  cblob["created"], "%Y-%m-%dT%H:%M:%SZ"),
                              created_by=cblob["createdBy"],
                              profile=pl)


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

# The expanded versions have the creationInfo key


def person_dict_p(p):
    # converts a Person object into a dictionary
    return({"spdxId": p.spdx_id,
            "type": "Person",
            "creationInfo": created_dict(p.creation_info)})


def org_dict_p(o):
    # converts an Organization object into a dictionary
    return({"spdxId": o.spdx_id,
            "type": "Organization",
            "creationInfo": created_dict(o.creation_info)})


def app_dict_p(app):
    # converts a Package object into a dictionary
    return({"spdxId": app.spdx_id,
            "name": app.name,
            "packageVersion": app.package_version,
            "type": "Package",
            "creationInfo": created_dict(app.creation_info)})


def relationship_dict_p(rel):
    # converts a Relationship object into a dictionary
    return({"spdxId": rel.spdx_id,
            "fromElement": rel.from_element,
            "relationshipType": camel_case(rel.relationship_type.name),
            "to": rel.toi,
            "creationInfo": created_dict(rel.creation_info)})


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


def make_elements_p(elements):
    # Similar to the above implementation except the CreationInfo is preserved
    elblob = {"person": [],
              "organization": [],
              "package": []}
    for el in elements:
        # introspection may not be possible in some languages, in which
        # case, something needs to store the class name in the object itself
        if el.__class__.__name__ == "Person":
            elblob["person"].append(person_dict_p(el))
        if el.__class__.__name__ == "Organization":
            elblob["organization"].append(org_dict_p(el))
        if el.__class__.__name__ == "Package":
            elblob["package"].append(app_dict_p(el))
    return elblob


def read_elements(docblob):
    # Parse an SPDX 3.0 blob and return a list of elements
    # This implementation checks for a document CreationInfo and assumes that
    # if an element doesn't have a CreationInfo, the document CreationInfo
    # is used create the elements
    elements = []
    if "creationInfo" in docblob.keys():
        # there is a document level CreationInfo
        cinfo = dict_created(docblob["creationInfo"])
    for key in docblob["elements"].keys():
        if key == "person":
            for pblob in docblob["elements"][key]:
                if "creationInfo" in pblob.keys():
                    # create a new CreationInfo object
                    pcinfo = mint(pblob["creationInfo"]["createdBy"],
                                  pblob["creationInfo"]["profile"],
                                  pblob["creationInfo"]["createdUsing"])
                    elements.append(model.Person(pblob["spdxId"],
                                                 creation_info=pcinfo))
                else:
                    elements.append(model.Person(pblob["spdxId"],
                                                 creation_info=cinfo))
        if key == "organization":
            for oblob in docblob["elements"][key]:
                if "creationInfo" in oblob.keys():
                    # create a new CreationInfo object
                    ocinfo = mint(oblob["creationInfo"]["createdBy"],
                                  oblob["creationInfo"]["profile"],
                                  oblob["creationInfo"]["createdUsing"])
                    elements.append(model.Organization(oblob["spdxId"],
                                                       creation_info=ocinfo))
                else:
                    elements.append(model.Organization(oblob["spdxId"],
                                                       creation_info=cinfo))
        if key == "package":
            for pkblob in docblob["elements"][key]:
                if "creationInfo" in pkblob.keys():
                    # create a new CreationInfo object
                    pkcinfo = mint(pkblob["creationInfo"]["createdBy"],
                                   pkblob["creationInfo"]["profile"],
                                   pkblob["creationInfo"]["createdUsing"])
                    elements.append(software.Package(pkblob["spdxId"],
                                                     pkblob["name"],
                                                     creation_info=pkcinfo))
                else:
                    elements.append(software.Package(pkblob["spdxId"],
                                                     pkblob["name"],
                                                     creation_info=cinfo))
    return elements


def get_integrity(filename):
    # Read a local file, calculate its hash and return an IntegrityMethod
    # object
    with open(filename, 'rb') as f:
        content = f.read()
    return model.Hash(model.HashAlgorithm.sha256,
                      hashlib.sha256(content).hexdigest())
