import json
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


def mint(agents, spdx_id):
    # Create a CreationInfo object to be used throughout the document
    return model.CreationInfo(spdx_id=spdx_id,
                              spec_version=Version('3.0.0'),
                              created=datetime.utcnow(),
                              created_by=agents,
                              profile=[model.ProfileIdentifierType.CORE,
                                       model.ProfileIdentifierType.SOFTWARE])


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

# The compact versions of these functions do not include the
# creation_info key


def person_dict(p):
    # converts a Person object into a dictionary
    return({"spdxId": p.spdx_id})


def org_dict(o):
    # converts an Organization object into a dictionary
    return({"spdxId": o.spdx_id})


def app_dict(app):
    # converts a Package object into a dictionary
    return({"spdxId": app.spdx_id,
            "name": app.name})


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
            "to": rel.to})


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


def generate():
    # Ids use URNs: https://en.wikipedia.org/wiki/Uniform_Resource_Name
    person_id = "urn:jane-doe-1@acme.com-76010e36-20e3-11ee-be56-0242ac120002"
    org_id = "urn:acme.com-4fe40e24-20e3-11ee-be56-0242ac120002"
    ts_id = "urn:sbom-acme-timestamp-5cfc33f3-9a0b-436c-8d81-bc8d9ed8ae25"
    # Assuming CreationInfo is mandatory for all elements
    # Creating the whole thing in one shot
    ts = mint([person_id, org_id], ts_id)
    # Now create the agent objects
    person = model.Person(person_id,
                          creation_info=ts)
    org = model.Organization(org_id,
                             creation_info=ts)
    # Software package produced
    app = software.Package("urn:product-acme-application-1.3-8f833b36-"
                           "20e3-11ee-be56-0242ac120002",
                           "acme-application",
                           ts)
    rel = model.Relationship("urn:relationship-acme-app-8f833b36-20e3-11ee-be56-0242ac120002",
                             app.spdx_id,
                             model.relationship.RelationshipType.AVAILABLE_FROM,
                             [person.spdx_id, org.spdx_id],
                             creation_info=ts)
    doc = model.SpdxDocument(spdx_id="urn:sbom-acme-application-8f833b36-20e3"
                             "-11ee-be56-0242ac120002",
                             name="acme-application",
                             element=["urn:product-acme-application-1.3-8f833"
                                      "b36-20e3-11ee-be56-0242ac120002",
                                      "urn:acme.com-4fe40e24-20e3-11ee-be56-"
                                      "0242ac120002",
                                      "urn:jane-doe-1@acme.com-76010e36-20e3-"
                                      "11ee-be56-0242ac120002"],
                             root_element=["urn:product-acme-application-1.3-"
                                           "8f833b36-20e3-11ee-be56-0242ac120"
                                           "002"],
                             creation_info=ts)
    # only the docblob has the creation info
    # Although the model requires the creation_info to be mandatory,
    # the serialization does not require it
    docblob = doc_dict(doc)
    elements = []
    elements.append(app)
    elements.append(person)
    elements.append(org)
    docblob["elements"] = make_elements(elements)
    docblob["relationships"] = [relationship_dict(rel)]
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
