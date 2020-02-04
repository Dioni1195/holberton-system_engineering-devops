#!/usr/bin/python3
""" This module is to do get """
import json
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1]))

    username = response.json()['username']

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])

    tasks = requests.get("{}".format(url)).json()
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        list_task = []
        for task in tasks:
            list_task.append({'task': task['title'],
                             'completed': task['completed'],
                              'username': username})
        dict_rep = {argv[1]: list_task}
        json.dump(dict_rep, jsonfile)
