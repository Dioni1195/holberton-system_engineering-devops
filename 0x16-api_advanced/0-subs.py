#!/usr/bin/python3
""" function that contain the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and 
    returns the number of subscribers 
    (not active users, total subscribers) 
    for a given subreddit. 
    """
    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit),headers={'User-Agent': 'Dioni'})
    if response.status_code == 404:
        return 0
    return response.json()['data']['subscribers']
