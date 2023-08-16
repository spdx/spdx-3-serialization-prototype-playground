import json
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software

import utils


def generate():
    # In this example, the container is provided by just the organization
    org_alpine_id = "urn:alpinelinux.org-2386480c-2434-433e-a0dc-eb10c5742ad8"
    # It is known what organization provides openssl
    org_openssl_id = "urn:openssl.org-0d106fcc-20e6-11ee-be56-0242ac120002"
    # This generation conforms to the core and software profile
    profiles = [model.ProfileIdentifierType.core,
                model.ProfileIdentifierType.software]
    # Create CreationInfo for the sbom
    ts = utils.mint([org_alpine_id],
                    profiles,
                    "container_compact.py")
    # Use CreationInfo when creating the org
    org_alpine = model.Organization(org_alpine_id,
                                    creation_info=ts)
    org_openssl = model.Organization(org_openssl_id,
                                     creation_info=ts)
    # Software package produced
    container = software.Package("urn:alpine-latest-4b36aed8-e41b-49f6-a5a7-8dbbcc54323d",
                                 "alpine-container",
                                 ts)
    openssl = software.Package("urn:openssl-3.0.4-cf812fb8-20e3-11ee-be56-0242ac120002",
                               "openssl",
                               ts,
                               package_version="3.0.4")
    rel1 = model.Relationship("urn:relationship-alpine-dfd8aed6-6899-4c01-8e56-01da8f3fccb1",
                              container.spdx_id,
                              model.relationship.RelationshipType.availableFrom,
                              [org_alpine.spdx_id],
                              creation_info=ts)
    rel2 = model.Relationship("urn:relationship-openssl-287295f7-894f-461b-a35a-22dbc37ae3f7",
                              container.spdx_id,
                              model.relationship.RelationshipType.contains,
                              [openssl.spdx_id],
                              creation_info=ts)
    rel3 = model.Relationship("urn:relationship-openssl-supplier-2e8c0ad2-0541-4ea5-99db-fab4a5e7395e",
                              openssl.spdx_id,
                              model.relationship.RelationshipType.availableFrom,
                              [org_openssl.spdx_id],
                              creation_info=ts)
    doc = model.SpdxDocument(spdx_id="urn:sbom-container-2df5b73b-e79b-4fbb-8a18-a60c383e6ce9",
                             name="alpine-container",
                             element=[container.spdx_id,
                                      openssl.spdx_id,
                                      org_alpine.spdx_id,
                                      org_openssl.spdx_id],
                             root_element=[container.spdx_id],
                             creation_info=ts)
    docblob = utils.doc_dict(doc)
    elements = []
    elements.append(container)
    elements.append(openssl)
    elements.append(org_alpine)
    elements.append(org_openssl)
    docblob["elements"] = utils.make_elements(elements)
    relationships = []
    relationships.append(utils.relationship_dict(rel1))
    relationships.append(utils.relationship_dict(rel2))
    relationships.append(utils.relationship_dict(rel3))
    docblob["relationships"] = relationships
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
