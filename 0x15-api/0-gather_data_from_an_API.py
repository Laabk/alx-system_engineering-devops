#!/usr/bin/python3
"""
A Script that uses JSONPlaceholder API to get information about an employee
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    re = requests.get(user)
    json_o = re.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    re = requests.get(todos)
    tasks = re.json()
    _task = []
    for ttask in tasks:
        if ttask.get('completed') is True:
            _task.append(ttask)

    print("({}/{}):".format(len(_task), len(tasks)))
    for ttask in _task:
        print("\t {}".format(ttask.get("title")))
