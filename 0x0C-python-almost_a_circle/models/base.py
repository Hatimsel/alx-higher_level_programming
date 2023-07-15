#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    def to_dictionary(self):
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        # list_dicts = [vars(obj) for obj in list_objs]
        # list_dicts = Base.to_dictionary(list_objs)
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        data = cls.to_json_string(list_dicts)
        class_name = cls.__name__
        with open(f"{class_name}.json", "w") as f:
            # json.dump(data, f)
            f.write(data)
