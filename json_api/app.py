import json
import requests


def query_api(query):
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    result = json.loads(response.text)
    # result = json.dumps(response.json())
    print(result)

if __name__ == '__main__':
    query_api("")