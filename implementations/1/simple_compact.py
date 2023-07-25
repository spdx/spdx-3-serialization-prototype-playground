import json
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software


def mint(agents, spdx_id):
    # Create a CreationInfo object to be used throughout the document
    return model.CreationInfo(spdx_id=spdx_id,
                              spec_version=Version('3.0.0'),
                              created=datetime.utcnow(),
                              created_by=agents,
                              profile=[model.ProfileIdentifierType.CORE,
                                       model.ProfileIdentifierType.SOFTWARE])


def created_dict(cinfo):
    profiles = []
    for pro in cinfo.profile:
        profiles.append(pro.name)
    return({"spdx_id": cinfo.spdx_id,
            "spec_version": f"{cinfo.spec_version.major}.{cinfo.spec_version.minor}.{cinfo.spec_version.patch}",
            "created": cinfo.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "created_by": cinfo.created_by,
            "profile": profiles,
            "data_license": cinfo.data_license,
            "created_using": cinfo.created_using})


def person_dict(p):
    return({"spdx_id": p.spdx_id})


def org_dict(o):
    return({"spdx_id": o.spdx_id})


def app_dict(app):
    return({"spdx_id": app.spdx_id,
            "name": app.name})


def doc_dict(doc):
    return({"spdx_id": doc.spdx_id,
            "name": doc.name,
            "element": doc.element,
            "root_element": doc.root_element,
            "creation_info": created_dict(doc.creation_info)})


def relationship_dict(rel):
    return({"spdx_id": rel.spdx_id,
            "from_element": rel.from_element,
            "relationship_type": rel.relationship_type.name,
            "to": rel.to})


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
    elements.append(app_dict(app))
    elements.append(person_dict(person))
    elements.append(org_dict(org))
    docblob["elements"] = elements
    docblob["relationships"] = [relationship_dict(rel)]
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
