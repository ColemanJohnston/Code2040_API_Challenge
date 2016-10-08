#Author: Coleman Johnston
#Date: 30 September 2016
#Description: Code2040 API challenge step 2.
import requests 
import json

def main():
    token = #put token here
    repo = "https://github.com/ColemanJohnston/Code2040_API_Challenge.git"
    url = "http://challenge.code2040.org/api/reverse" 

    payload = {'token' : token , 'github' : repo}

    r = requests.post(url , json = payload ) 

    url = "http://challenge.code2040.org/api/reverse/validate"

    payload["string"] = r.text[::-1]    

    r = requests.post(url , json = payload )

    print r.text

main()