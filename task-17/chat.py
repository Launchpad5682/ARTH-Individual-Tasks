import socket
import threading as thread
import time
import os 

# udp protocol
udp = socket.SOCK_DGRAM
# net address family : ip_v4
afm = socket.AF_INET

# Own IP Address
own_ip = input("Enter your own IP address: ")
port = 1234

# receiver's IP address
recv_ip = input("Enter the receiver's IP address: ")

# Instructing the type of protocol and IP_type
s = socket.socket(afm, udp)

# binding the IP address and port to create a socket
s.bind((own_ip, port))

# Receive function
def recv():
    while True:
        msg_recv = s.recvfrom(1024)
        if msg_recv[0].decode() == "quit":
            print("User left")
            os._exit(1)

        print(msg_recv[1][0] + " : " + msg_recv[0].decode())


# Send function
def send():
    while True:
        msg = input("Type your message: ")
        s.sendto(msg.encode(), (recv_ip, port))
        if msg == "quit":
            print("Chat ended")
            os._exit(1)


# send and receive threads
send_thread = thread.Thread(target=send)
recv_thread = thread.Thread(target=recv)

# starting threads
send_thread.start()
recv_thread.start()