#!/usr/bin/python3
"""
Using a REST API, and a given employee ID,
return info about their TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()

    TOTAL = len(employee_todos)
    completed = [t for t in employee_todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(completed), TOTAL))
    for task in completed:
        print("\t {}".format(task.get("title")))
