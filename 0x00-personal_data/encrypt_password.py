#!/usr/bin/env python3
""" Task-1 hashing passwords with bcrypt  """

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        hashed_password (bytes): The salted and hashed password as a byte
        string.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password stored in the database.
        password (str): The password to be validated.

    Returns:
        valid (bool): True if the password matches the hashed password,
        False otherwise.
    """
    password_bytes = password.encode('utf-8')
    valid = bcrypt.checkpw(password_bytes, hashed_password)
    return valid
