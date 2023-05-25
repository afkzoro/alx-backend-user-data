#!/usr/bin/env python3
""" Task-0 """
import re


def filter_datum(fields, redaction, message, separator):
    """ Filter Datum """
    pattern = '|'.join([f'(?<={field}=)[^;]*' for field in fields])
    return re.sub(pattern, redaction, message)
