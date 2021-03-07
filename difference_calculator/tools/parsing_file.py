"""Parsing the file"""

import json
import yaml
from pathlib import Path


def parsing_file(path_file):
    """Parsing the file"""
    file_extension = Path(path_file).suffix
    if file_extension == '.json' or file_extension == '.JSON':
        return json.load(open(path_file))
    elif file_extension == '.yml' or file_extension == '.YAML':
        return yaml.safe_load(open(path_file))
