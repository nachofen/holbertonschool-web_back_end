#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """ lists all documents in a collection:
    Args: mongo collection
    Returns: an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
    """
    docs_list = []
    for doc in mongo_collection.find():
        docs_list.append(doc)
    return docs_list
