#!/usr/bin/python3
"""the queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

from requests import get


def top_ten(subreddit):
    """ this is the queries to Reddit API
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    usr_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    resp = get(url, headers=usr_agent, params=params)
    res = resp.json()

    try:
        data = res.get('data').get('children')

        for d in data:
            print(d.get('data').get('title'))

    except Exception:
        print("None")
