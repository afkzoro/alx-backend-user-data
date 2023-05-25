#!/usr/bin/env python3
""" Task-0 """
import re


def filter_datum(fields, redaction, message, separator):
    """_summary_

    Args:
        fields (_type_): _description_
        redaction (_type_): _description_
        message (_type_): _description_
        separator (_type_): _description_

    Returns:
        _type_: _description_
    """
    pattern = '|'.join([f'(?<={field}=)[^{separator}]*' for field in fields])
    return re.sub(pattern, redaction, message)
