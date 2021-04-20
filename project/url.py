import requests

def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False

def process_response(url):
    r = requests.get(url)
    return r.content