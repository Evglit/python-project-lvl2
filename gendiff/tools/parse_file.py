"""Parsing the file"""

import json
import yaml
from pathlib import Path


def get_dict_from_file(path_file):
    """Parse the file and return dict"""
    file_extension = Path(path_file).suffix
    if file_extension.lower() == '.json':
        return json.load(open(path_file))
    elif file_extension == '.yml' or file_extension == '.YAML':
        return yaml.safe_load(open(path_file))
