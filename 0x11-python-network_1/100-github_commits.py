#!/usr/bin/python3
"""
Python script that takes 2 arguments to list 10 commits (from the most recent to oldest)
of a repository given repository name and owner name using the GitHub API
Usage: ./100-github_commits.py <repository name> <owner name>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
