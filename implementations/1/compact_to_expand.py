import json
from semantic_version import Version
from datetime import datetime
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software
import sys


def created_dict(cinfo):
    profiles = []
    for pro in cinfo.profile:
        profiles.append(pro.name)
    return({"spdxId": cinfo.spdx_id,
            "specVersion": f"{cinfo.spec_version.major}.{cinfo.spec_version.minor}.{cinfo.spec_version.patch}",
            "created": cinfo.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "createdBy": cinfo.created_by,
            "profile": profiles,
            "dataLicense": cinfo.data_license,
            "createdUsing": cinfo.created_using})


def person_dict(p):
    return({"spdxId": p.spdx_id,
            "creationInfo": created_dict(p.creation_info)})


def org_dict(o):
    return({"spdxId": o.spdx_id,
            "creationInfo": created_dict(o.creation_info)})


def app_dict(app):
    return({"spdxId": app.spdx_id,
            "name": app.name,
            "creationInfo": created_dict(app.creation_info)})


def doc_dict(doc):
    return({"spdxId": doc.spdx_id,
            "name": doc.name,
            "element": doc.element,
            "rootElement": doc.root_element,
            "creationInfo": created_dict(doc.creation_info)})


def relationship_dict(rel):
    return({"spdxId": rel.spdx_id,
            "fromElement": rel.from_element,
            "relationshipType": rel.relationship_type.name,
            "to": rel.to,
            "creationInfo": created_dict(rel.creation_info)})


def expand(docblob):
    # Read an SPDX 3.0 compacted blob and return an SPDX 3.0 expanded blob
    # Replicate the document level CreationInfo blob into all elements
    # create the CreationInfo object first so it can be used throughout the doc
    pl = []
    for profile in docblob["creationInfo"]["profile"]:
        pl.append(model.ProfileIdentifierType[profile])
    cinfo = model.CreationInfo(spdx_id=docblob["creationInfo"]["spdxId"],
                               spec_version=Version(docblob["creationInfo"]["specVersion"]),
                               created=datetime.strptime(docblob["creationInfo"]["created"], "%Y-%m-%dT%H:%M:%SZ"),
                               created_by=docblob["creationInfo"]["createdBy"],
                               profile=pl)
    # now create the agents
    # although when creating the document, we knew the subclass of the Agent,
    # we don't know it now
    agent_list = []
    for agent_id in docblob["creationInfo"]["createdBy"]:
        agent_list.append(model.Agent(spdx_id=agent_id, creation_info=cinfo))

    # the list of elements could be any element type, including agents
    # we will filter the agents out
    not_agents = []
    for element in docblob["elements"]:
        if element["spdxId"] not in docblob["creationInfo"]["createdBy"]:
            not_agents.append(element)

    # we don't know what kind of element the root element is and we cannot
    # abstract it so we will guess from the profile
    elements = []
    if "SOFTWARE" in docblob["creationInfo"]["profile"]:
        # this is a very weak assertion because from the data, we don't know
        # what the concrete class is
        for element in not_agents:
            elements.append(software.Package(
                spdx_id=element["spdxId"],
                name=element["name"],
                creation_info=cinfo))

    # we have better luck with relationships
    relationships = []
    for rel in docblob["relationships"]:
        relationships.append(model.Relationship(
            rel["spdxId"],
            rel["fromElement"],
            model.RelationshipType[rel["relationshipType"]],
            rel["to"],
            creation_info=cinfo))

    # now we create a Document with the same information
    doc = model.SpdxDocument(spdx_id=docblob["spdxId"],
                             name=docblob["name"],
                             element=docblob["element"],
                             root_element=docblob["rootElement"],
                             creation_info=cinfo)
    docblob = doc_dict(doc)
    elblobs = []
    # the order of the elements may change here but we still don't
    # know if this implementation will work for all concrete element
    # classes
    for agent in agent_list:
        # we don't know what kind of agent this is
        elblobs.append(org_dict(agent))
    for element in elements:
        elblobs.append(app_dict(element))
    docblob["elements"] = elblobs
    relblobs = []
    for rel in relationships:
        relblobs.append(relationship_dict(rel))
    docblob["relationships"] = relblobs
    print(json.dumps(docblob))


if __name__ == "__main__":
    docblob = json.loads(sys.stdin.buffer.read())
    expand(docblob)
