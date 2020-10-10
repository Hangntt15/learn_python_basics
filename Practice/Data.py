import requests
import json


def data():
    url = 'http://51.83.36.184:20001/'
    my_obj = {
        "id": 1,
        "jsonrpc": "1.0",
        "method": "getpdestate",
        "params": [
            {
                "BeaconHeight": 68806
            }

        ]
    }
    t = requests.post(url, json=my_obj, headers={'Content-Type': 'application/json'})
    res = json.loads(t.text)
    return res
