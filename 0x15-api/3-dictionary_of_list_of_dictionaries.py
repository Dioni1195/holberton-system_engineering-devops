#!/usr/bin/python3
""" This module is to do get """
import json
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get('https://jsonplaceholder.typicode.com/users')

    users = response.json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        dict_rep = {}
        for user in users:
            username = user['username']
            id = user['id']
            url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
                  .format(id)
            tasks = requests.get("{}".format(url)).json()
            list_task = []
            for task in tasks:
                list_task.append({'task': task['title'],
                                 'completed': task['completed'],
                                  'username': username})
            dict_rep[id] = list_task
        json.dump(dict_rep, jsonfile)
