#!/usr/bin/python3
"""
Module for basemodel class
defines all common attributes/methods for other classes
for airbnb clone project - the console
"""

import uuid
import datetime
from models import storage

class BaseModel:
    """Class that define all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialities base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a nice print of the base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the date of update"""
        self.updated_at = datetime.datetime.now()
        storage.save(self)

    def to_dict(self):
        """Returns a new dict"""
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict        