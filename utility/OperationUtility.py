import ast
import json
import requests
import jsonschema
from jsonschema import validate
import re

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

    def getResponseJsonKeyValue(self, jsonData, key):
        if key in jsonData['data']['product']:
            return(jsonData['data']['product'][key])
        else:
            return("KEY NOT FOUND")

    
    def checkKeyexistInArray(self, listItems, key):
        for index,ele in enumerate(listItems):
            if key in listItems[index]['sizes']:
               return True

        return False

    def getMediaDataKeysFromArray(self, listItems, key):
        
        if key not in {"small","xsmall"}:
            for index,ele in enumerate(listItems):
                if key in listItems[index]:
                    return (listItems[index][key])

        for index,ele in enumerate(listItems):
            if key in listItems[index]['sizes']:
                return (listItems[index]['sizes'][key])

        return False
    
    def getLocationKeysInArray(self, listItems, key):
        for index,ele in enumerate(listItems):
            if key in listItems:
                return (listItems[key])

        return False

    def validate_longitude(self, longitude):
        try:
            longitude = str(longitude)
            if re.fullmatch("^([+-])?(?:180(?:\\.0{1,6})?|((?:|[1-9]|1[0-7])[0-9])(?:\\.[0-9]{1,7})?)$", longitude):
                return True
            else:
                return False
        except:
            return False

    def validate_latitude(self, latitude):
        try:

            latitude = str(latitude)
            if re.fullmatch("^([+-])?(?:90(?:\\.0{1,6})?|((?:|[1-8])[0-9])(?:\\.[0-9]{1,7})?)$", latitude):
                return True
            else:
                return False
        except:
            return False

    def validate_url(self,url):
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return (re.match(regex, url) is not None) 
    

