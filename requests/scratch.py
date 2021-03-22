##################
# Using API tasks from RealPython - Python JSON website
##################

import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todo2 = response.json()
#todos = json.loads(response.text)
#print(todos)
print(todo2)

# Either:
# 1. todos = response.json()
# 2. todos = json.loads(response.text)     - Serialises the object into a String


# Each user has an unique user ID, and each task has a boolean completed property.
# Which users have completed the most tasks.

# Map of userID to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user
for todo in todo2:
    if todo['completed']:
        try:
            # Increment the existing user's count
            todos_by_user[todo['userId']] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1
            todos_by_user[todo['userId']] = 1

# Create a sorted list of (userID, num_complete) pairs.
# items() returns key, value pairs from dictionary 
top_users = sorted(todos_by_user.items(), key = lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed the maximum number of TODOs
users = []
for user, num_complete, in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_user = " and ".join(users)

# In interactive window, run script and type:
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_user} completed {max_complete} TODOs")
### Need to clean that print statement from the old version to new.

# Create a JSON file to contain the completed TODOs for each of the users who completed the
# maximum number of TODOs

# Define a function to filter out completed TODOs of users with max completed TODOs
def keep(todo):
    is_complete = todo2['completed']
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count

# Write filetered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todo2))
    json.dump(filtered_todos, data_file, indent = 2)







