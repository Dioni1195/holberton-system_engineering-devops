#!/usr/bin/python3
""" function that contain the number of subscribers"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.
    """
    response = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                            format(subreddit), headers={'User-Agent': 'Dioni'})
    if response.status_code == 404:
        print(None)
    else:
        for hot in response.json()['data']['children']:
            print(hot['data']['title'])
