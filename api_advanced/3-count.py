#!/usr/bin/python3
"""Python Script to count keywords in hot article titles."""
import requests


def count_words(sub_reddit, word_list, after=None, word_counts=None):
    """
    Recursively query Reddit API and count keyword occurrences in hot titles.

    Args:
        sub_reddit: the name of the subreddit to query.
        word_list: list of keywords to count.
        after: pagination token for next page.
        word_counts: dictionary tracking keyword counts.
    """
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            w = word.lower()
            word_counts[w] = word_counts.get(w, 0)

    if sub_reddit is None or not isinstance(sub_reddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(sub_reddit)
    headers = {"User-Agent": "linux:3-count:v1.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "")
        title_words = title.lower().split()
        for t_word in title_words:
            for keyword in word_counts:
                if t_word == keyword:
                    word_counts[keyword] += 1

    after = data.get("after")
    if after is not None:
        return count_words(sub_reddit, word_list, after, word_counts)

    sorted_words = sorted(word_counts.items(),
                          key=lambda kv: (-kv[1], kv[0]))
    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))
