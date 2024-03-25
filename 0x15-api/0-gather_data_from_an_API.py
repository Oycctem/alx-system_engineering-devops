#!/usr/bin/python3
""" a Python script that for a given employee ID, returns information """
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    data = user_response.json()

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo['completed']]
    ncomplt_tasks = len(completed_tasks)

    tasks = len(todos_data)

    print(f"Employee {data['name']} is done with tasks", end='')
    print(f"({ncomplt_tasks}/{tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")
