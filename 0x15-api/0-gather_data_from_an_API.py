#!/usr/bin/python3
# script that gather data from an API

import requests
from sys import argv

if __name__ == "__main__":
    task_completed = 0
    user = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    param = {"userId": argv[1]}
    user_response = requests.get(user_url + f"{user}").json()
    todo_data = requests.get(todo_url, params=param).json()
    for item in todo_data:
        if (item["completed"]):
            task_completed += 1
    tasks = len(todo_data)
    print(f"Employee {user_response['name']} is done with tasks", end="")
    print(f"({task_completed}/{tasks}):")
    for item in todo_data:
        if (item["completed"]):
            print(f"\t {item['title']}")
