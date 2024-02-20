#!/usr/bin/python3
"""
A Script that uses JSONPlaceholder API to get information about employee
"""
import json
import requests as re


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = re.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({usr.get("id"): [{
            "username": usr.get("username"),
            "task": el.get("title"),
            "completed": el.get("completed")
        } for el in re.get(url + "todos",
            params={"userId": usr.get("id")}).json()]
            for usr in user}, jsonfile)
