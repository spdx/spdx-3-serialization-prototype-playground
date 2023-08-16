import json
from spdx_tools.spdx3 import model
from spdx_tools.spdx3.model import software

import utils


def generate():
    # The containerization process is done by a Dockerfile created
    # by the author. However, Acme Company has a policy of placing IP ownership
    # with the company.
    org_id = "urn:acme.com-4fe40e24-20e3-11ee-be56-0242ac120002"
    # This generation conforms to the core and software profile
    profiles = [model.ProfileIdentifierType.core,
                model.ProfileIdentifierType.software]
    # This document has a specific CreationInfo
    ts = utils.mint([org_id],
                    profiles,
                    "app_in_container.py")
    org = model.Organization(org_id,
                             creation_info=ts)
    # For clarity, we will define all the element ids here
    container_id = "urn:product-acme-container-1.3-58636866-50ba-4a50-a11b-818ff4f5bdc7"
    doc_id = "urn:sbom-acme-container-1.3-4ab0bd4b-064b-4e36-94ac-3459a2425ba8"
    rel_container_id = "urn:relationship-container-9c83c478-0338-4930-89ea-b74585e29a8f"
    rel_supplier_id = "urn:relationship-acme-supplier-c6484017-073c-4741-9af0-126358382b28"
    # The container is the root element
    container = software.Package(container_id,
                                 "acme/acme-container",
                                 ts,
                                 package_version="1.3")
    # We want to link other SPDX documents to this one
    # Each document has an identifier, an integrity method
    app_sbom_ext_id = "urn:external-sbom-acme-app-5a6e83d0-e085-43d3-93dd-d53db6a6b19c"
    alpine_sbom_ext_id = "urn:external-sbom-alpine-d847e068-e912-4a61-9d4c-0b13ac56d565"

    # Ideally, this should be something given via a command line, API, or
    # config file. For now, we will explicitly provide which files represent
    # what software component
    app_sbom_integrity = utils.get_integrity("acme_compact.json")
    alpine_sbom_integrity = utils.get_integrity("alpine_compact.json")

    # We link the documents using the ExternalMap
    app_emap = model.ExternalMap(app_sbom_ext_id,
                                 [app_sbom_integrity],
                                 "acme_compact.json")
    alpine_emap = model.ExternalMap(alpine_sbom_ext_id,
                                    [alpine_sbom_integrity],
                                    "alpine_compact.json")

    # Relationship is used to define the relationships among the elements
    rel_supplier = model.Relationship(rel_supplier_id,
                                      container.spdx_id,
                                      model.relationship.RelationshipType.availableFrom,
                                      [org.spdx_id],
                                      creation_info=ts)
    rel_contains = model.Relationship(rel_container_id,
                                      container.spdx_id,
                                      model.relationship.RelationshipType.contains,
                                      [alpine_sbom_ext_id, app_sbom_ext_id])

    # Now create the document
    doc = model.SpdxDocument(spdx_id=doc_id,
                             name="acme-container",
                             element=[container.spdx_id,
                                      org.spdx_id],
                             root_element=[container.spdx_id],
                             creation_info=ts)

    # Now build the JSON payload
    docblob = utils.doc_dict(doc)
    elements = []
    elements.append(container)
    elements.append(org)
    docblob["elements"] = utils.make_elements(elements)
    imports = []
    imports.append(utils.external_map_dict(app_emap))
    imports.append(utils.external_map_dict(alpine_emap))
    docblob["imports"] = imports
    relationships = []
    relationships.append(utils.relationship_dict(rel_supplier))
    relationships.append(utils.relationship_dict(rel_contains))
    docblob["relationships"] = relationships
    print(json.dumps(docblob))


if __name__ == "__main__":
    generate()
