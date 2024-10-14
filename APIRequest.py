import requests

url ="http://ws.chez-wam.info/"

def get_data(code):
    response = requests.get(url + code).json()
    print(response['images'][0])
    print(response['price'])
    print(response['title'])

get_data("B09V356ZBZ")
