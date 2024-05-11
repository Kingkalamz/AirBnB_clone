#!/usr/bin/python3

import models
from uuid import uuid4
from datetime import datetime

"""Defines the BaseModel class."""


class BaseModel:
    """Represent the BaseModel class of the AirBnB project
    """
    def __init__(self):
        """Initializes a new BameModel
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        def save(self):
            """Updates updated_at with the current datetime"""

            self.updated_at = datetime.today()

        def to_dict(self):
            """Returns the dictionary of the BaseModel instance"""

            new_dict = self.__dict__.copy()
            new_dict["__class__"] = self.__class.__name
            new_dict["created_at"] = self.created_at.isoformat()
            new_dict["updated_at"] = self.updated_at.isoformat()
            return (new_dict)

        def __str__(self):
            """Returns the print/string representation
            of the BaseModel instance
            """

            class_name = self.__class__.__name__
            return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
