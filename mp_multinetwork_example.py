import multiprocessing as mp
import socket
import pickle as p

def onConnection(conn, addr):
    full_data = b''
    print(f"{addr[0]}::{addr[1]} has established connection")
    while True:
        # Establish connection with client.
        data = conn.recv(1024)
        if data:
            decoded = p.loads(data)
            print(decoded)
        else:
            break
    conn.close()

if __name__ == '__main__':
    s = socket.socket()
    port = 12345
    s.bind(('', port))
    procs = []
    while 1:
        s.listen(5)
        conn, addr = s.accept()
        procs.append( mp.Process(target = onConnection, args = (conn, addr,)) )
        procs[-1].start()# no need to join()

'''
###########CLIENT CODE##############
import socket
import time as t
import numpy as np
import pickle as p
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server
s.connect(('192.168.0.8', port))

# receive data from the server and decoding to get the string.
#print (s.recv(1024).decode())
i = 1
while True:
    t.sleep(1)
    to_send = f"hello people {i}"
    to_send = p.dumps(to_send)
    s.sendall(to_send)
    i += 1
    if i == 10:
        break# i am lazy
s.close()
'''