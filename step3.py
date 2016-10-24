#Author: Coleman Johnston
#Date: 30 September 2016
#Description: Code2040 API challenge step 3.
import requests 
import json
import ast

 

def main():
    token = # Put API Token here 
    url = "http://challenge.code2040.org/api/" 

    payload = {'token' : token}

    r = requests.post(url + "haystack", json = payload ) 

    data = r.text

    data = ast.literal_eval(data)

    needle = data["needle"]

    haystack = data["haystack"]

    payload["needle"] = haystack.index(needle)

    r = requests.post(url + "haystack/validate", json = payload )

    print(r.text)        

main()


