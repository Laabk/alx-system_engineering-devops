#!/usr/bin/python3
"""
A Script that uses JSONPlaceholder API to get information about employee
"""
import json
import requests as re
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = re.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    todo = re.get(url + "todos", params={"user_id": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": e.get("title"),
            "completed": e.get("completed"),
            "username": username} for e in todo]},jsonfile)
