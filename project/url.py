import requests
import json

def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False

def process_response(url):
    r = requests.get(url)
    return r.content

def google_query(query):
    # url = "http://www.google.com"
    url = "http://api.open-notify.org/astros.json"
    # params = {'callback' : 'CALLBACK'}
    # params = {number: 1,  }
    resp = requests.get(url)
    # resp.raise_for_status()
    # result = json.dumps(resp)
    for i in resp:
        aa = json.dumps(i)
        print(aa)
    print(result)

if __name__ == '__main__':
    google_query('bananas')