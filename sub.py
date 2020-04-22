import socket
import json
from transmitJSON import recvJSON, sendJSON

with open('subinfo.json') as f:
    msg = json.load(f)

s = socket.socket()
s.connect(("localhost",3001))
sendJSON(s,msg)