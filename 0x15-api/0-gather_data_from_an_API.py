#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))
