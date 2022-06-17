from requests import get, post
import sys
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv('HOST_NAME')
port = os.getenv('PORT')
url = hostname + ':' + str(port)


def invalid():
    print("Invalid command")


def print_response(response):
    print('Status code:', response.status_code)
    print(response.text)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        invalid()
    elif args[0] == 'set':
        if len(args) < 3:
            invalid()
        else:
            response = post(url + '/set', json={'key': args[1], 'value': args[2]})
            print_response(response)
    elif args[0] == 'get':
        if len(args) < 2:
            invalid()
        else:
            response = get(url + '/get', params={'key': args[1]})
            print_response(response)
    elif args[0] == 'history':
        if len(args) < 2:
            invalid()
        else:
            response = get(url + '/history', params={'key': args[1]})
            print_response(response)
    else:
        invalid()
