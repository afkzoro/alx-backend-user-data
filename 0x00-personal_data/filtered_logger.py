#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    pattern = fr'({separator.join(fields)})=[^;]+'
    return re.sub(pattern, f'{redaction}={redaction}', message)
