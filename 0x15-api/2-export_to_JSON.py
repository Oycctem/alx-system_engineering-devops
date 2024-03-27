#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    user_tasks = [{"task": t.get("title"), 
                   "completed": t.get("completed"), 
                   "username": username} for t in todos]

    filename = f"{user_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump({user_id: user_tasks}, jsonfile)
