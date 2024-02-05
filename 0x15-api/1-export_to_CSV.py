#!/usr/bin/python3
"""
script that gather data from an API
and export them in the CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    param = {"userId": argv[1]}
    user_response = requests.get(user_url + f"{user}").json()
    todo_data = requests.get(todo_url, params=param).json()

    with open("USER_ID.csv", mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in todo_data:
            writer.writerow([user, user_response["username"],
                             item["completed"], item["title"]])
