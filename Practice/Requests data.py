import requests
import json


def get_data(url, method_name, params):
    body = {
        "jsonrpc": "1.0",
        "method": method_name,
        "params": params,
        "id": 1
    }
    headers = {'Content-Type': 'application/json'}
    t = requests.post(url, json=body, headers=headers, timeout=10)
    res = json.loads(t.text)
    return res


def get_publickeyfrompaymentaddress(url, paymentaddress):
    method_name = 'getpublickeyfrompaymentaddress'
    params = [paymentaddress]
    return get_data(url, method_name, params)


def get_balancebyprivatekey(url, privatekey):
    method_name = 'getbalancebyprivatekey'
    params = [privatekey]
    return get_data(url, method_name, params)


def get_listprivacycustomtokenbalance(url, privatekey):
    method_name = 'getlistprivacycustomtokenbalance'
    params = [privatekey]
    return get_data(url, method_name, params)


def get_balanceprivacycustomtoken(url, privatekey1, privatekey2):
    method_name = 'getbalanceprivacycustomtoken'
    params = [privatekey1, privatekey2]
    return get_data(url, method_name, params)


def get_burningaddress(url):
    method_name = 'getburningaddress'
    params = []
    return get_data(url, method_name, params)


def get_listunspentoutputtokens(url, privateKey, tokenID):
    method_name = 'listunspentoutputtokens'
    params = [
        0,
        999999,
        [
            {
                "PrivateKey": privateKey,
                "StartHeight": 0,
                "tokenID": tokenID
            }
        ]
    ]
    return get_data(url, method_name, params)

# -------------------------------------------------
# test_run:
# print(get_publickeyfrompaymentaddress('http://51.83.36.184:20001/', "12Rz8iQVFFaSmpDtsZ5Yv43hYnDeCZeKBE77r7VsSQ5dQNa35bKCoDfKak3u75hhpLPdPetvYtEkX4aE5RNNXWZ1p3z73BJRgbtvEu4"))
# print(get_balancebyprivatekey('http://51.83.36.184:20001/',"112t8rnX5E2Mkqywuid4r4Nb2XTeLu3NJda43cuUM1ck2brpHrufi4Vi42EGybFhzfmouNbej81YJVoWewJqbR4rPhq2H945BXCLS2aDLBTA"))
# print(get_listprivacycustomtokenbalance('http://51.83.36.184:20001/',"112t8rnX5E2Mkqywuid4r4Nb2XTeLu3NJda43cuUM1ck2brpHrufi4Vi42EGybFhzfmouNbej81YJVoWewJqbR4rPhq2H945BXCLS2aDLBTA"))
