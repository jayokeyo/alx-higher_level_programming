#!/usr/bin/python3
'''
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Usage: ./2-post_email.py <url> <email>
'''

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data).encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))

