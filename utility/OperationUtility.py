import ast
import json
import requests
import jsonschema
from jsonschema import validate

class Utility:  
    def readSchemaFromFile(self, path):
        with open(path) as f:
            data = f.read()
        return json.loads(data)

    def validateJsonWithSchema(self, s, jsonData):
        try:
            validate(instance=jsonData, schema=s)
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)
            print(err.json_path)
            return False
        return True

    def validateJSON(self, j):
        try:
            r1 = json.loads(j)
        except ValueError as err:
            print("THIS IS VALUE ERROR" + err)
            return False
        return True





