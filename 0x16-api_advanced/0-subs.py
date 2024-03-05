#!/usr/bin/python3
"""this queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests as req
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    usr_agent = 'Google Chrome Version 81.0.4044.129'

    headers = {
        'User-Agent': usr_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = req.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    dicti = resp.json()
    if 'data' not in dicti:
        return 0
    if 'subscribers' not in dicti.get('data'):
        return 0
    return resp.json()['data']['subscribers']
