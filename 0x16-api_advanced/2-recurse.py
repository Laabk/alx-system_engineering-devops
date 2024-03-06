#!/usr/bin/python3
"""this queries the Reddit API and prints
the top ten hot posts of a subreddit"""

import requests as req
after = None

def recurse(subreddit, hot_list=[]):
    """returs top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'after': after}
    resp = req.get(url, params=param, headers=user_agent,
            allow_redirects=False)

    if resp.status_code == 200:
        afr_dta = resp.json().get("data").get("after")
        if afr_dta is not None:
            after = afr_dta
            recurse(subreddit, hot_list)
        al_ttle = resp.json().get("data").get("children")
        for titl in al_ttle:
            hot_list.append(titl.get("data").get("title"))
        return hot_list
    else:
        return (None)
