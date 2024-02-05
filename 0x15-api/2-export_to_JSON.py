#!/usr/bin/python3
"""
script that gather data from an API
and export them in JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    param = {"userId": argv[1]}
    user_response = requests.get(user_url + f"{user}").json()
    todo_data = requests.get(todo_url, params=param).json()
    username = user_response["username"]
    with open("{}.json".format(user), "w") as file:
        json.dump({user: [{"task": item['title'],
                           "completed": item['completed'],
                           "username": username} for item in todo_data]},
                  file)
