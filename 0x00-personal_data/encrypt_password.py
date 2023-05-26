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
