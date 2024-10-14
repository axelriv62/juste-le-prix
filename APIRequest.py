import requests

url = "http://ws.chez-wam.info/"

def get_data(code):
    response = requests.get(url + code).json()
    return {
        'image': response['images'][0],
        'price': response['price'],
        'title': response['title']
    }

