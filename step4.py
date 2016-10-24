#Author: Coleman Johnston
#Date: 23 October 2016
#Description: Code2040 API challenge step 4.
import requests 
import json
import ast

 

def main():
    token = # Put API Token here
    url = "http://challenge.code2040.org/api/" 

    payload = {'token' : token}

    r = requests.post(url + "prefix", json = payload ) 

    data = r.text

    data = ast.literal_eval(data)

    prefix = data["prefix"]

    array = data["array"]

    
    result = []

    for item in array:
        if(item.find(prefix) != 0):
            result.append(item)
            
    payload["array"] = result

    r = requests.post(url + "prefix/validate", json = payload )

    print(r.text)        

main()


