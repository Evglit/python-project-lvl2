"""to parse text"""

import json
import yaml


def to_parse(arg):
    if arg[-5:] == '.json':
        return json.load(open(arg))
    elif arg[-4:] == '.yml':
        with open(arg) as f:
            return yaml.safe_load(f)
