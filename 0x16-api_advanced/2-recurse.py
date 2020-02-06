#!/usr/bin/python3
""" function that contain the number of subscribers"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """ function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.
    """
    if after is None:
        return hot_list
    header = {'User-Agent': 'Dioni'}
    if len(hot_list) == 0:
        response = requests.get('https://www.reddit.com/r/{}/hot.json'.
                                format(subreddit), headers=header)
    else:
        parms = {'after': after, 'limit': count}
        response = requests.get('https://www.reddit.com/r/{}/hot.json'.
                                format(subreddit),
                                headers=header, params=parms)

    if response.status_code == 404:
        return None
    else:
        for hot in response.json()['data']['children']:
            hot_list.append(hot['data']['title'])
        after = response.json()['data']['after']
        count = 100
        return recurse(subreddit, hot_list, count, after)
