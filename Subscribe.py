import socket
import json
import sys

def recvJSON(socket):
	finished = False
	msg = ''
	while not finished:
		msg += socket.recv(4096).decode('utf8')
		try:
			data = json.loads(msg)
			finished = True
		except json.JSONDecodeError:
			pass
	return data

def sendJSON(socket, data):
	msg = json.dumps(data).encode('utf8')
	total = 0
	while total < len(msg):
		sent = socket.send(msg[total:])
		total += sent

msg = {'matricules': ['17341', '17367'], 'port': 8000, 'name': 'FrigoFri'}

s = socket.socket()
s.connect(("localhost",3001))
sendJSON(s,msg)