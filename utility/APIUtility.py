import ast
import json
import requests

class APIUtility:
  def __init__(self):
    self.base_url = ""
    self.response_code = 0
    self.responseJson = {}
    self.responseHeader = {}
    self.responseTime = 0
  
  def post_request(self, payload):
    post_url = self.base_url
    response = requests.post(url=self.base_url, json={"query": payload})
    self.responseTime = response.elapsed.total_seconds()
    self.response_code = response.status_code
    self.responseJson = response.json()
    self.responseHeader = response.headers
    return response
  
  def setbaseURL(self, url):
    self.base_url = url

  def getResponseJson(self):
    return responseJson
