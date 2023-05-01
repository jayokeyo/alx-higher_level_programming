#!/usr/bin/python3
'''
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
The email must be sent in the variable email
Usage: ./6-post_email.py <url> <email>
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data)
    print(response.text)
