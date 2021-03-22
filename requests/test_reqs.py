import requests
import json
from datetime import datetime


# Get returns a response object
page = requests.get('https://httpbin.org/get.doesntexist')


# Returns a status code of API

# * print(page.status_code)


# Often there will be multiple APIs available on a particular server.
# Each of these APIs are called endpoints

# There is a built in JSON decoder: ".json()"

Open_Notify_API = requests.get("http://api.open-notify.org/astros.json")
# * print(Open_Notify_API.json())

# The JSON library has two main functions: 
# json.dumps() - Takes in a Python Object and converts (dumps) it to a string
# json.loads() - Takes a JSON string, and converts (loads) it to a Python object



def jprint(obj):
    # Create a formatted string  of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent = 4)
    print(text)

# Remove comment when finished
# * jprint(Open_Notify_API.json())

# The above API endpoint doesn't take any parameters
# It's common to have a endpoint that requires us to specify parameters
# Below endpoint requires lat and long

parameters = {
    "lat" : 40.71,
    "lon": -74
}

API_pass = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
#jprint(API_pass.json())

# Extract the "response" key
pass_times = API_pass.json()['response']
jprint(pass_times)

rise_times = []
# Loop to extract information
for d in pass_times:
    time = d['risetime']
    rise_times.append(time)
print("The rise times are:", rise_times)

# Times are printed in format timestamp, counting the seconds from January 1st 1970

times = []
for rt in rise_times:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print("formatted times", times)



myAPP = requests.get("http://127.0.0.1:5000/")
print(myAPP.status_code)


obj2 = myAPP.json()['aquisition Type']
print(obj2)


# Python's context manager
#with open("myAPP", "/Users/stuartsmith/Documents/JSON_Dumps.txt")

with open("new_JSON_data_file.json", "w") as write_file:
    json.dump(["people"], write_file)


# Dump takes 2 positonal arguments
# 1. The data object to be serialized
# 2. The file like object to which the bytes will be written

# Dumps takes 1 argument, because you're not writing to disk