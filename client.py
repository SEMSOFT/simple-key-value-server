from requests import get, post
import sys

hostname = 'http://127.0.0.1'
port = 5000
url = hostname + ':' + str(port)

def invalid():
    print("Invalid command")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        invalid()
    elif args[0] == 'set':
        if len(args) < 3:
            invalid()
        response = post(url + '/set', data={'key': args[1], 'value': args[2]})
        print(response.text)
    elif args[0] == 'get':
        if len(args) < 2:
            invalid()
        response = get(url + '/get', params={'key': args[1]})
        print(response.text)
    elif args[0] == 'history':
        if len(args) < 2:
            invalid()
        response = get(url + '/history', params={'key': args[1]})
        print(response.text)
    else:
        print("Invalid command")