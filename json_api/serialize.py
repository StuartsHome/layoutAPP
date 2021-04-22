import requests
import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# Desirializing into a file
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

json_string = json.dumps(data)
print(json_string)

"""
If you’ve pulled JSON data in from another program or have otherwise obtained a string of JSON formatted data in Python,
you can easily deserialize that with loads(), which naturally loads from a string
"""

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

json_serialized_string = json.loads(json_string)
print(json_serialized_string)