import json
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software


def mint(agents):
    # Create a CreationInfo object to be used throughout the document
    return model.CreationInfo(spdx_id="urn:depcreation-eb9d3ab5-2cc4-4e32-882a-4252fc8e0b1b",
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
    return({"spdx_id": p.spdx_id,
            "creation_info": created_dict(p.creation_info)})


def org_dict(o):
    return({"spdx_id": o.spdx_id,
            "creation_info": created_dict(o.creation_info)})


def app_dict(app):
    return({"spdx_id": app.spdx_id,
            "name": app.name,
            "creation_info": created_dict(app.creation_info)})


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
    # Create identity id's first
    org_id = "urn:alpinelinux.org-2386480c-2434-433e-a0dc-eb10c5742ad8"
    # Create CreationInfo for the sbom
    ts = mint([org_id])
    # Create the org
    org = model.Organization(org_id,
                             creation_info=ts)
    # Software package produced
    container = software.Package("urn:alpine-latest-4b36aed8-e41b-49f6-a5a7-8dbbcc54323d",
                                 "alpine-container",
                                 ts)
    openssl = software.Package("urn:openssl-35e25462-2f81-4ef4-80f1-135b85632b43",
                               "openssl",
                               ts)
    rel1 = model.Relationship("urn:relationship-alphine-dfd8aed6-6899-4c01-8e56-01da8f3fccb1",
                              container.spdx_id,
                              model.relationship.RelationshipType.AVAILABLE_FROM,
                              [org.spdx_id],
                              creation_info=ts)
    rel2 = model.Relationship("urn-relationship-openssl-287295f7-894f-461b-a35a-22dbc37ae3f7",
                              container.spdx_id,
                              model.relationship.RelationshipType.CONTAINS,
                              [openssl.spdx_id],
                              creation_info=ts)
    doc = model.SpdxDocument(spdx_id="urn:sbom-container-2df5b73b-e79b-4fbb-8a18-a60c383e6ce9",
                             name="alpine-container",
                             element=["urn:alpine-latest-4b36aed8-e41b-49f6-a5a7-8dbbcc54323d",
                                      "urn:openssl-35e25462-2f81-4ef4-80f1-135b85632b43",
                                      "urn:relationship-alphine-dfd8aed6-6899-4c01-8e56-01da8f3fccb1",
                                      "urn-relationship-openssl-287295f7-894f-461b-a35a-22dbc37ae3f7"],
                             root_element=["urn:alpine-latest-4b36aed8-e41b-49f6-a5a7-8dbbcc54323d"],
                             creation_info=ts)
    docblob = doc_dict(doc)
    elements = []
    elements.append(app_dict(container))
    elements.append(app_dict(openssl))
    elements.append(org_dict(org))
    docblob["elements"] = elements
    relationships = []
    relationships.append(relationship_dict(rel1))
    relationships.append(relationship_dict(rel2))
    docblob["relationships"] = relationships
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
