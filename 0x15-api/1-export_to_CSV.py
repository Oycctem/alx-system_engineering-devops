#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([
                f"{user_id}", f"{username}",
                f"{t.get('completed')}", f"{t.get('title')}"
            ])
