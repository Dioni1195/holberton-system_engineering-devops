#!/usr/bin/python3
""" This module is to do get """
import json
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1]))

    name = response.json()['name']

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])

    tasks = requests.get("{}".format(url)).json()
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        dict_rep = {argv[1]: tasks}
        json.dump(dict_rep, jsonfile)
