#!/usr/bin/python3

"""Define a FileStorage ckass."""

import json
from models.base_model import BaseModel


class ileStorage:
    """Represent an abstracted storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary -_objects"""

        return (FileStorage.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        ocname = obj.__class.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_pat"""

        odict = FileStorage.__object
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.____file_path, "w") as f:
            json.dumps(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects exists ;
        otherwise, do nothing."""

        try:
            with open(FileStorage.__filepath) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
