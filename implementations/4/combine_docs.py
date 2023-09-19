import json
import sys
from spdx_tools.spdx3 import model

import utils


def combine(doc1, doc2):
    # Given two SPDX documents, combine them into one document
    # We assume Acme Company is combining the documents, so the document
    # level id's hold
    org_id = "urn:acme.com-4fe40e24-20e3-11ee-be56-0242ac120002"
    profiles = [model.ProfileIdentifierType.core,
                model.ProfileIdentifierType.software]
    ts = utils.mint([org_id],
                    profiles,
                    "combine_docs.py")
    org = model.Organization(org_id,
                             creation_info=ts)
    # create elements from the two docs
    elements = []
    elements.append(org)
    for el in utils.read_elements(doc1):
        elements.append(el)
    for el in utils.read_elements(doc2):
        elements.append(el)
    # create a new document
    doc_id = "urn:sbom-envelope-04bf01ba-eb2a-409a-89c2-47a650e9bfd8"
    doc = model.SpdxDocument(spdx_id=doc_id,
                             name="containerized acme application",
                             element=[org_id],
                             root_element=[],
                             creation_info=ts)
    # convert the document into a JSON serialization
    docblob = utils.doc_dict(doc)
    # we'll preserve the input documents' CreationInfo
    docblob["elements"] = utils.make_elements_p(elements)
    print(json.dumps(docblob))


if __name__ == "__main__":
    # Assuming we are reading two documents and combining them
    with open(sys.argv[1]) as f:
        doc1 = json.load(f)
    with open(sys.argv[2]) as f:
        doc2 = json.load(f)
    combine(doc1, doc2)
