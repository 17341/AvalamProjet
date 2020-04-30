import socket
import json
import sys
from transmitJSON import sendJSON

msg = {'matricules': ['17341', '17367'], 'port': 8000, 'name': 'FrigoFri'}

s = socket.socket()
s.connect(("localhost",3001))
sendJSON(s,msg)