# simple key-value server

## Server
The server is a service providing REST API with Flask-restful.

The server has three commands:
- Receives a (key, value) and stores it.
- Returns the last value assigned to a specified key. If the key does not exist, throws an error.
- Returns the history of values of a specified key. If the key does not exist, throws an error.

## Client
The client is a simple service that sends requests to the server and gets responses.

## Running the project
In the first step, you need to clone the repository on your system.

The project is written with python, so you must have installed python3 on your system.

### Install dependencies
You can install the dependencies that are needed for the project with pip using this command:
```
pip install -r requirements.txt
```

### Run server
You must define hostname and port as the arguments of the code. You can run the server using this command:
```
python server.py <hostname> <port>
```
For example, with this command we can run the server on localhost:5000:

```
python server.py 127.0.0.1 5000
```

### Run client
The client will send requests to localhost:5000 by default. So you can change it from the code.

The followings are the commands for sending a request from the client to the server:
- Set a new item with (key, value):
```
python client.py set key value
```
- Get the last value assigned to the key:
```
python client.py get key
```
- Get the history of values of the key:
```
python client.py history key
```
