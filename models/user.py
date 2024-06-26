#!/usr/bin/python3

"""Defines a class user."""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from BaseModel
        Public class attributes:
            email: (str) - user's email
            password: (str) - user's password
            first_name: (str) - user's first name
            last_name: (str) - user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
