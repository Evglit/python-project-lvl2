"""Open files"""

import json
import yaml


def open_file(arg):
    """Open a file by path"""
    if arg[-5:] == '.json':
        return json.load(open(arg))
    elif arg[-4:] == '.yml':
        with open(arg) as f:
            return yaml.safe_load(f)
