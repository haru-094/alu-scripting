#!/usr/bin/python3
"""Python Script get data from the reddit api for subscriber."""
import requests


def number_of_subscribers(sub_reddit):
    """
    Getting the number of subscribe.

    Args:
        sub_reddit: the name of the subreddit to query.

    Returns:
        The number of total subscribers, or 0 if the subreddit is invalid.
    """
    if sub_reddit is None or not isinstance(sub_reddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(sub_reddit)
    headers = {"User-Agent": "linux:0-subs:v1.0 (by /u/alu_student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
