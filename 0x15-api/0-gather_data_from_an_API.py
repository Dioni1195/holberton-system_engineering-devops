#!/usr/bin/python3
""" This module is to do get """
import requests
from sys import argv

if __name__ == "__main__":
    data_usr = {'id': argv[1]}

    response = requests.get('https://jsonplaceholder.typicode.com/users',
                            params=data_usr)

    json_usr = response.json()
    name = json_usr[0]['name']

    data_task = {'userId': argv[1]}

    url_com = 'https://jsonplaceholder.typicode.com/'
    parm_com = 'todos?completed=true'

    response_complete = requests.get("{}{}".format(url_com, parm_com),
                                     params=data_task)

    url_inm = 'https://jsonplaceholder.typicode.com/'
    parm_inm = 'todos?completed=false'

    response_incomplete = requests.get("{}{}".format(url_inm, parm_inm),
                                       params=data_task)

    json_task_complete = response_complete.json()
    json_task_incomplete = response_incomplete.json()

    num_incomplete = len(json_task_incomplete)
    num_complete = len(json_task_complete)

    print("Employee {} is done with tasks({}/{}):".
          format(name, num_complete, num_complete + num_incomplete))
    for task in json_task_complete:
        print("\t {}".format(task['title']))
