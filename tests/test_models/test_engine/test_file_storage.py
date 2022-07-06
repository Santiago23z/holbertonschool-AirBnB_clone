#!/usr/bin/python3
""" Tets from file storage
"""



import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """
    """

    def setUp(self):
        """Method setup"""
        pass

    def resetStorage(self):
        """"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """"""
        self.resetStorage()
        pass

    def test_instance(self):
        """"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_attr(self):
        """"""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_all(self, line):
        """"""
        self.resetStorage()
        object = eval(line)()
        storage.new(object)
        key = f"{type(object).__name__}.{object.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], object)

    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.test_all("BaseModel")

    def test_all_user(self):
        """Tests all() method for User."""
        self.test_all("User")

    def test_all_state(self):
        """Tests all() method for State."""
        self.test_all("State")

    def test_all_city(self):
        """Tests all() method for City."""
        self.test_all("City")

    def test_all_amenity(self):
        """Tests all() method for Amenity."""
        self.test_all("Amenity")

    def test_all_place(self):
        """Tests all() method for Place."""
        self.test_all("Place")

    def test_all_review(self):
        """Tests all() method for Review."""
        self.test_all("Review")

    def test_all_mult(self, line):
        """"""
        self.resetStorage()
        dict_objects = [eval(line)() for i in range(1000)]
        [storage.new(obj) for obj in dict_objects]
        self.assertEqual(len(dict_objects), len(storage.all()))
        for s in dict_objects:
            key = f"{type(s).__name__}.{object.s}"
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], s)

    def test_all_multiple_base_model(self):
        """Tests all() method with many objects."""
        self.test_all_mult("BaseModel")

    def test_all_multiple_user(self):
        """Tests all_multiple() method for User."""
        self.test_all_mult("User")

    def test_all_multiple_state(self):
        """Tests all_multiple() method for State."""
        self.test_all_mult("State")

    def test_all_multiple_city(self):
        """Tests all_multiple() method for City."""
        self.test_all_mult("City")

    def test_all_multiple_amenity(self):
        """Tests all_multiple() method for Amenity."""
        self.test_all_mult("Amenity")

    def test_all_multiple_place(self):
        """Tests all_multiple() method for Place."""
        self.test_all_mult("Place")

    def test_all_multiple_review(self):
        """Tests all_multiple() method for Review."""
        self.test_all_mult("Review")

    def test_new(self, line):
        """"""
        self.resetStorage()
        new = eval(line)()
        storage.new(new)
        key = f"{type(new).__name__}.{new.id}"
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], new)

    def test_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.test_new("BaseModel")

    def test_new_user(self):
        """Tests new() method for User."""
        self.test_new("User")

    def test_new_state(self):
        """Tests new() method for State."""
        self.test_new("State")

    def test_new_city(self):
        """Tests new() method for City."""
        self.test_new("City")

    def test_new_amenity(self):
        """Tests new() method for Amenity."""
        self.test_new("Amenity")

    def test_new_place(self):
        """Tests new() method for Place."""
        self.test_new("Place")

    def test_new_review(self):
        """Tests new() method for Review."""
        self.test_new("Review")

    def test_save(self, line):
        """"""
        self.resetStorage()
        new_obj = eval(line)()
        storage.new(new_obj)
        key = f"{type(new_obj).__name__}.{new_obj.id}"
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        new_dict = {key: new_obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(new_dict)))
            f.seek(0)
            self.assertEqual(json.load(f), new_dict)

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.test_save("BaseModel")

    def test_save_user(self):
        """Tests save() method for User."""
        self.test_save("User")

    def test_save_state(self):
        """Tests save() method for State."""
        self.test_save("State")

    def test_save_city(self):
        """Tests save() method for City."""
        self.test_save("City")

    def test_save_amenity(self):
        """Tests save() method for Amenity."""
        self.test_save("Amenity")

    def test_save_place(self):
        """Tests save() method for Place."""
        self.test_save("Place")

    def test_save_review(self):
        """Tests save() method for Review."""
        self.test_save("Review")

    def test_reload(self, line):
        """"""
        self.resetStorage()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        new_reload = eval(line)()
        storage.new(new_reload)
        key = f"{type(new_reload).__name__}.{new_reload.id}"
        storage.save()
        storage.reload()
        self.assertEqual(new_reload.dict(), storage.all()[key].to_dict())

    def test_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.test_reload("BaseModel")

    def test_reload_user(self):
        """Tests reload() method for User."""
        self.test_reload("User")

    def test_reload_state(self):
        """Tests reload() method for State."""
        self.test_reload("State")

    def test_reload_city(self):
        """Tests reload() method for City."""
        self.test_reload("City")

    def test_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.test_reload("Amenity")

    def test_reload_place(self):
        """Tests reload() method for Place."""
        self.test_reload("Place")

    def test_reload_review(self):
        """Tests reload() method for Review."""
        self.test_reload("Review")


if __name__ == "__main__":
    unittest.main()
