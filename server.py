import socket
import time
from decimal import Decimal

def main():
    given_host = '127.0.0.1'  # You can put whatever you want here.
    given_portal = 5000     # I inserted a high number because the first 4000+ portals are the default one.


    socket_obj = socket.socket()    # Socket's creation.
    socket_obj.bind((given_host, given_portal))     # Connect the socket with the host ip an the portal number.
    beg_time = time.time() # Keeping the starting time to see how much time does this chatting took.
    socket_obj.listen(1) # One connection at the time
    client, adress = socket_obj.accept() # Accepted the specific client with the specific address.
    print("Connected address: " , str(adress)) # Testify the connection by printing the address.
    while not False:
        data = client.recv(1024).decode('utf-8') # 1024 raw bytes at a time + utf after [receive message].
        if not data:
            break
        print(data)
        data = input() # Typing a message for the client and,
        client.send(data.encode('utf-8')) # here I am sending it.
    client.close()
    b = Decimal(time.time() - beg_time)
    output = round(b, 2)
    print("Your conversation kept: ",output, " seconds")    # Printing the final time of the conversation

if __name__ == "__main__":

    main()
