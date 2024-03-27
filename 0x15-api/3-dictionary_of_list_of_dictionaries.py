#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    all_users = requests.get(url + "users").json()

    all_user_tasks = {}
    for user in all_users:
        user_id = user['id']
        username = user['username']
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        user_tasks = [{"username": username, "task": todo["title"], "completed": todo["completed"]} for todo in todos]
        all_user_tasks[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_user_tasks, json_file, separators=(',', ':'))
