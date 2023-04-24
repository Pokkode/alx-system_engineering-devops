#!/usr/bin/python3
"""
Script that uses JSONPlaceholder
API to get information about employee
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = "{}users/{}".format(url, sys.argv[1])
    res = requests.get(user)
    output = res.json()
    print("Employee {} is done with tasks".format(output.get('name')), end="")

    todos = "{}todos?userId={}".format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    task_list = []
    for task in tasks:
        if task.get('completed') is True:
            task_list.append(task)

    print("({}/{}):".format(len(task_list), len(tasks)))
    for task in task_list:
        print("\t {}".format(task.get("title")))
