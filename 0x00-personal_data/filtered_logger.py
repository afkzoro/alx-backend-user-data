#!/usr/bin/env python3
""" Task-0 """
import re


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join([f'(?<={field}=)[^{separator}]*' for field in fields])
    return re.sub(pattern, redaction, message)
