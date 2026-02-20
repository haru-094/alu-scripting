#!/usr/bin/python3
"""Python Script to get data from the Reddit API for top 10 hot posts."""
import requests


def top_ten(sub_reddit):
    """
    Getting the ttile for the first 10 hot post.

    Args:
        sub_reddit: the name of the subreddit to query.
    """
    if sub_reddit is None or not isinstance(sub_reddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(sub_reddit)
    headers = {"User-Agent": "linux:1-top_ten:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
