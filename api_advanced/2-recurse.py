#!/usr/bin/python3
"""Python Script to get all hot article titles from Reddit."""
import requests


def recurse(sub_reddit, hot_list=[], after=None):
    """
    Recursively get all hot article titles for a given subreddit.

    Args:
        sub_reddit: the name of the subreddit to query.
        hot_list: list to accumulate article titles.
        after: pagination token for the next page of results.

    Returns:
        A list of all hot article titles, or None if invalid subreddit.
    """
    if sub_reddit is None or not isinstance(sub_reddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(sub_reddit)
    headers = {"User-Agent": "linux:2-recurse:v1.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        if not hot_list:
            return None
        return hot_list

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None

    return recurse(sub_reddit, hot_list, after)
