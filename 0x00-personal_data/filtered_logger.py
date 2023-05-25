#!/usr/bin/env python3
""" Task-0 """
import re


def filter_datum(fields, redaction, message, separator):
    """ Filter datum """
    pattern = fr'({separator.join(fields)})=[^;]+'
    return re.sub(pattern, f'{redaction}={redaction}', message)
