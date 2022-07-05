#!/usr/bin/python3
"""testing state file"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import pep8
import unittest
State = state.State

class TestStateDocs(unittest.testCase):
    """checking documenytation and review class style"""
    @classmethod
    def setUpClass(cls):
        """set up for the doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)
        
    def test_pep8_conformance_state(self):
        """checking that state.py allows to PEP8"""
        pep8s = pep8s.check_files(['models/state.py'])
        result = pep8.StyleGuide(quiet=True)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in state.py")
        
    def test_pep8_conformance_test_state(self):
        """checking that test_state.py allows to PEP8"""
        pep8s = pep8s.check_files(['tests/test_models/test_state.py'])
        result = pep8.StyleGuide(quiet=True)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in state.py")
        
    def test_state_module_docstring(self):
        """checking for state class docstring"""
        self.assertIsNot(state.__doc__, None,
                         "docstring module not found in state.py")
        self.assertTrue(len(state.__doc__) >= 1,
                        "docstring module not found in state.py")
                        
    def test_state_class_docstring(self):
        """checking for state class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "docstring not found in state class")
        self.assertTrue(len(state.__doc__) >= 1,
                        "docstring not found in state class")
        
    def test_state_func_docstring(self):
        """test for the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
            
class TestState(unittest.TestCase):
    """TestState: to test class state"""
    def test_save_Method(self):
        """Function: test_saveMethod to test save instance method"""
        new_st = State()
        new_st.save()
        self.assertNotEqual(new_st.created_at, new_st.updated_at)
        
    def test_to_dic_Method(self):
        """Function: test_to_dictMethod to test to_dict method"""
        new_stdic = State()
        state_dict = new_stdic.to_dict()
        self.assertEqual(new_stdic.__class__.__name__, "State")
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertIsInstance(state_dict['id'], str)
        
    def test_has_methods(self):
        """Function: test_hasmethods if it has all basic attrbs
            from BaseModel"""
        new_st = State()
        self.assertTrue(hasattr(new_st, "__init__"))
        self.assertTrue(hasattr(new_st, "__str__"))
        self.assertTrue(hasattr(new_st, "save"))
        self.assertTrue(hasattr(new_st, "to_dict"))
        
    def test_hasatribs(self):
        """Function: test_hasatribs to test if it has attributes"""
        new_stattr = State()
        self.assertTrue(hasattr(new_stattr, "name"))
        self.assertTrue(hasattr(new_stattr, "created_at"))
        self.assertTrue(hasattr(new_stattr, "updated_at"))
        self.assertTrue(hasattr(new_stattr, "id"))
        self.assertTrue("id" in new_stattr.__dict__)
        
    def test_type(self):
        """pendiente"""
        new_sttype = State()
        self.assertEqual(type(new_sttype.name), str)
        
    def test_inherit(self):
        j = State()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)
        
if __name__ == '__main__':
    unittest.main()
