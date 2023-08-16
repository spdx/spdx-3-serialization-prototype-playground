import json
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software

import utils


def generate():
    # Ids use URNs: https://en.wikipedia.org/wiki/Uniform_Resource_Name
    person_id = "urn:jane-doe-1@acme.com-76010e36-20e3-11ee-be56-0242ac120002"
    org_id = "urn:acme.com-4fe40e24-20e3-11ee-be56-0242ac120002"
    # This generation conforms to the core and software profile
    profiles = [model.ProfileIdentifierType.core,
                model.ProfileIdentifierType.software]
    # Assuming CreationInfo is mandatory for all elements
    # Creating the whole thing in one shot
    ts = utils.mint([person_id, org_id],
                    profiles,
                    "app_compact.py")
    # Now create the agent objects
    person = model.Person(person_id,
                          creation_info=ts)
    org = model.Organization(org_id,
                             creation_info=ts)
    # Software package produced
    app = software.Package("urn:product-acme-application-1.3-8f833b36-"
                           "20e3-11ee-be56-0242ac120002",
                           "acme-application",
                           ts,
                           package_version="1.3")
    rel = model.Relationship("urn:relationship-acme-app-8f833b36-20e3-11ee-be56-0242ac120002",
                             app.spdx_id,
                             model.relationship.RelationshipType.availableFrom,
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
    docblob = utils.doc_dict(doc)
    elements = []
    elements.append(app)
    elements.append(person)
    elements.append(org)
    docblob["elements"] = utils.make_elements(elements)
    docblob["relationships"] = [utils.relationship_dict(rel)]
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
