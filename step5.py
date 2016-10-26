#Author: Coleman Johnston
#Date: 26 October 2016
#Description: Code2040 API challenge step 5.
import requests
import json
import ast
import datetime
from datetime import timedelta


def main():
    token = # Put API Token here
    url = "http://challenge.code2040.org/api/" 

    payload = {'token' : token}

    r = requests.post(url + "dating", json = payload )

    data = r.text

    data = ast.literal_eval(data)

    datestamp = data["datestamp"]

    interval = data["interval"]

    date = datetime.datetime.strptime( datestamp, "%Y-%m-%dT%H:%M:%S" + datestamp[len(datestamp) - 1] )

    addTime = timedelta(seconds = interval) #convert interval into data type that can be added to time

    date = date + addTime
        
    payload["datestamp"] = date.isoformat() + datestamp[len(datestamp) - 1]

    r = requests.post(url + "dating/validate", json = payload )

    print(r.text)

main()