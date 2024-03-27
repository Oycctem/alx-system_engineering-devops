#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user_data['name']

    todo_data = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    progress_message = (
        f"Employee {employee_name} is done with tasks"
        f"({completed_tasks}/{total_tasks}):"
    )
    print(progress_message)
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
