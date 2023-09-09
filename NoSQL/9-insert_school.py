#!/usr/bin/env python3
""" task 9 """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
    - mongo_collection: The MongoDB collection object.
    - kwargs: Keyword arguments representing the fields and values to be inserted.

    Returns:
    - The id of the inserted school (typically, the _id field).
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
