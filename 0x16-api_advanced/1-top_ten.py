#!/usr/bin/python3
"""queries the Reddit API and prints
the top ten hot posts of a subreddit"""

import requests as req
import sys


def top_ten(subreddit):
    """ Queries to Reddit API involved"""
    usr_agent = 'Google Chrome Version 81.0.4044.129'

    headers = {
        'User-Agent': usr_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    resp = req.get(url, headers=headers, params=params,
            allow_redirects=False)
    if resp.status_code != 200:
        print(None)
        return
    dicti = resp.json()
    h_posts = dicti['data']['children']
    if len(h_posts) is 0:
        print(None)
    else:
        for pos in h_posts:
            print(pos['data'][
