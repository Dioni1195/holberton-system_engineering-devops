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
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            usr_id = task['userId']
            status = task['completed']
            title = task['title']
            writer.writerow({'USER_ID': usr_id, 'USERNAME': username,
                             'TASK_COMPLETED_STATUS': status,
                             'TASK_TITLE': title})
