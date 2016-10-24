#Author: Coleman Johnston
#Date: 30 September 2016
#Description: Code2040 API challenge step 1.   
import requests 
import json

def main():
    api_token = # Put API Token here
    gitHub_repo = "https://github.com/ColemanJohnston/Code2040_API_Challenge.git"
    url = "http://challenge.code2040.org/api/register"

    print(register(api_token,gitHub_repo,url))
    
def register(token, repo, url):
    payload = {'token' : token , 'github' : repo}

    r = requests.post(url , json = payload )

    return r.text

main()