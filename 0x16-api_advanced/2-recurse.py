#!/usr/bin/python3
"""this queries the Reddit API and prints
the top ten hot posts of a subreddit"""

import requests as req


def recurse(subreddit, hot_list=[], after=""):
    """ Queries to Reddit API """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Google Chrome Version 81.0.4044.129"
        }
    param = {
        "after": after,
        "limit": 100,
    }
    resp = req.get(url, headers=headers, params=param, allow_redirects=False)
    if resp.status_code == 404:
        return None
    else:
        pos = resp.json().get("data").get("children")
        h_list += [post.get("data").get("title") for post in pos]
        after = resp.json().get("data").get("after")
        if after is not None:
                recurse(subreddit, h_list, after)
        return h_list
