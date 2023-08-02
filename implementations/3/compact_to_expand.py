import json
from functools import reduce
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software
import sys


def camel_case(string):
    # Utility function to convert snake_case to camelCase
    # Used to satisty conventions described in `model`
    words = string.split("_")
    camel = words[0].lower() + ''.join(word.lower().title() for word in words[1:])
    return camel


def case_camel(string):
    # Utility function to convert camelCase into enums
    # We may not need this if the python tools can support it
    return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, string).upper()


def created_dict(cinfo):
    # converts a CreationInfo object into a dictionary
    profiles = []
    for pro in cinfo.profile:
        profiles.append(camel_case(pro.name))
    return({"spdxId": cinfo.spdx_id,
            "specVersion": f"{cinfo.spec_version.major}.{cinfo.spec_version.minor}.{cinfo.spec_version.patch}",
            "created": cinfo.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "createdBy": cinfo.created_by,
            "profile": profiles,
            "dataLicense": cinfo.data_license,
            "createdUsing": cinfo.created_using})

# The expanded version of the document contains creationInfo
# for every element


def person_dict(p):
    # converts a Person object into a dictionary
    return({"spdxId": p.spdx_id,
            "creationInfo": created_dict(p.creation_info)})


def org_dict(o):
    # converts an Organization object into a dictionary
    return({"spdxId": o.spdx_id,
            "creationInfo": created_dict(o.creation_info)})


def app_dict(app):
    # converts a Package object into a dictionary
    return({"spdxId": app.spdx_id,
            "name": app.name,
            "creationInfo": created_dict(app.creation_info)})


def doc_dict(doc):
    # converts a Document object into a dictionary
    return({"spdxId": doc.spdx_id,
            "name": doc.name,
            "element": doc.element,
            "rootElement": doc.root_element,
            "creationInfo": created_dict(doc.creation_info)})


def relationship_dict(rel):
    # converts a Relationship object into a dictionary
    return({"spdxId": rel.spdx_id,
            "fromElement": rel.from_element,
            "relationshipType": camel_case(rel.relationship_type.name),
            "to": rel.to,
            "creationInfo": created_dict(rel.creation_info)})


def make_elements(elements):
    # This implementation currently checks for just Person, Organization,
    # and Package but the logic should be the same for all concrete classes
    # "elements" is a list of multiple types of objects. This may not be
    # implementable in a strongly typed language unless polymorphism is
    # supported.
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


def read_elements(elblob, ts):
    # This implementation is the reverse of the above function
    # We also need the timestamp
    elements = []
    for key in elblob.keys():
        if key == "person":
            for pblob in elblob[key]:
                elements.append(model.Person(pblob["spdxId"],
                                             creation_info=ts))
        if key == "organization":
            for oblob in elblob[key]:
                elements.append(model.Organization(oblob["spdxId"],
                                                   creation_info=ts))
        if key == "package":
            for pkblob in elblob[key]:
                elements.append(software.Package(pkblob["spdxId"],
                                                 pkblob["name"],
                                                 creation_info=ts))
    return elements


def expand(docblob):
    # Read an SPDX 3.0 compacted blob and return an SPDX 3.0 expanded blob
    # Replicate the document level CreationInfo blob into all elements
    # create the CreationInfo object first so it can be used throughout the doc
    pl = []
    for profile in docblob["creationInfo"]["profile"]:
        pl.append(model.ProfileIdentifierType[profile.upper()])
    cinfo = model.CreationInfo(spdx_id=docblob["creationInfo"]["spdxId"],
                               spec_version=Version(docblob["creationInfo"]["specVersion"]),
                               created=datetime.strptime(docblob["creationInfo"]["created"], "%Y-%m-%dT%H:%M:%SZ"),
                               created_by=docblob["creationInfo"]["createdBy"],
                               profile=pl)

    # reading relationships is straightforward
    relationships = []
    for rel in docblob["relationships"]:
        relationships.append(model.Relationship(
            rel["spdxId"],
            rel["fromElement"],
            model.RelationshipType[case_camel(rel["relationshipType"])],
            rel["to"],
            creation_info=cinfo))

    # elements is more involved since we need to find out what objects are
    # available
    elements = read_elements(docblob["elements"], cinfo)

    # now we create a Document with the same information
    doc = model.SpdxDocument(spdx_id=docblob["spdxId"],
                             name=docblob["name"],
                             element=docblob["element"],
                             root_element=docblob["rootElement"],
                             creation_info=cinfo)
    docblob = doc_dict(doc)
    docblob["elements"] = make_elements(elements)
    relblobs = []
    for rel in relationships:
        relblobs.append(relationship_dict(rel))
    docblob["relationships"] = relblobs
    print(json.dumps(docblob))


if __name__ == "__main__":
    docblob = json.loads(sys.stdin.buffer.read())
    expand(docblob)
