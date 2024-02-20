#!/usr/bin/python3
"""
A Script that uses JSONPlaceholder API to get information about employee
"""
import csv
import requests as re
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = re.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    todo = re.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
            elm.get("title")]) for elm in todo]
