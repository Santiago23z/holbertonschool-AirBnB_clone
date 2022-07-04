#!/usr/bin/python3
"""module for user class AirBnb project"""

import mailbox
from ssl import _PasswordType
from unicodedata import name
from models.base_model import BaseModel

class User(BaseModel):
    """defines all instance attributes for a User instance

        Public class attributes:
        email <string>: User´s e-mailbox
        password <string>: User _Password
        fisrt_name <string>: User´s firs name
        last_name <string>: User´s last name
    """
    email = ""
    password = ""
    first_name = ""
    las_name = ""
    