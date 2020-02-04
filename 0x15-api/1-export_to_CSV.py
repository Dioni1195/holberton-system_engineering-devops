#!/usr/bin/python3
""" This module is to do get """
import csv
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1]))

    username = response.json()['username']

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])

    tasks = requests.get("{}".format(url)).json()
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            usr_id = task['userId']
            status = task['completed']
            title = task['title']
            writer.writerow([usr_id, username, status, title])
