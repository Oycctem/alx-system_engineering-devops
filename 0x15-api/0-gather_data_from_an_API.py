import requests
import sys


employee_id = sys.argv[1]

base_url = 'https://jsonplaceholder.typicode.com'

user_response = requests.get(f'{base_url}/users/{employee_id}')
user_data = user_response.json()

todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
todos_data = todos_response.json()

completed_tasks = [todo for todo in todos_data if todo['completed']]
num_completed_tasks = len(completed_tasks)

total_tasks = len(todos_data)

print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")

for task in completed_tasks:
    print(f"\t{task['title']}")
