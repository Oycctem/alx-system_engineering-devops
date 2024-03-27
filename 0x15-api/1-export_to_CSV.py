#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [
        (user.get("id"), user.get("name"), t.get("completed"), t.get("title"))
        for t in todos if t.get("completed")
    ]

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(completed_tasks)
