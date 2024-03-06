#!/usr/bin/python3
"""this queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """ this is the Queries to Reddit API
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    usr_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = get(url, headers=usr_agent)
    res = resp.json()

    try:
        return res.get('data').get('subscribers')

    except Exception:
        return 0
