#!/usr/bin/python3
"""this queries the Reddit API and prints
the top ten hot posts of a subreddit"""
import json
import requests as req


def count_words(subreddit, word_list, after="", count=[]):
    """count all wnd adds words" in the list"""

    if after == "":
        counts = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    requst = req.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if requst.status_code == 200:
        data = requst.json()

        for contnt in (data['data']['children']):
            for a_word in contnt['data']['title'].split():
                for d in range(len(word_list)):
                    if word_list[d].lower() == word.lower():
                        counts[d] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for d in range(len(word_list)):
                for i in range(d + 1, len(word_list)):
                    if word_list[d].lower() == word_list[i].lower():
                        save.append(i)
                        counts[d] += counts[i]

            for d in range(len(word_list)):
                for i in range(d, len(word_list)):
                    if (counts[i] > counts[d] or
                            (word_list[d] > word_list[i] and
                             counts[i] == counts[d])):
                        aux = counts[d]
                        counts[d] = counts[i]
                        counts[i] = aux
                        aux = word_list[d]
                        word_list[d] = word_list[i]
                        word_list[i] = aux

            for d in range(len(word_list)):
                if (counts[d] > 0) and d not in save:
                    print("{}: {}".format(word_list[d].lower(), counts[d]))
        else:
            count_words(subreddit, word_list, after, counts)
