import requests
import json

url = "https://api.spacexdata.com/v4/landpads"
response = requests.get(url)



'''
The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
'''

'''
The dumps() function is particularly useful as we can use it to print a formatted string
which makes it easier to understand the JSON output.
'''




def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print(response.status_code)
jprint(response.json())




