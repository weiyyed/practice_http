import json
import yaml
import os.path
from ate.exception import ParamsError

def load_testcase(filepath):
    suffix=os.path.splitext(filepath)[1]
    if suffix==".json":
        return load_json(filepath)
