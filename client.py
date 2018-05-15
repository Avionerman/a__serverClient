import socket

def main():
    given_host = '127.0.0.1'  # Here you can put whatever you want.
    given_portal = 5000     # I inserted a high number because the first 4000+ portals are the default one.

    socket_obj = socket.socket()
    socket_obj.connect((given_host, given_portal))

    msg = input()
    while msg != 'exit':
        socket_obj.send(msg.encode('utf-8'))    # Sending a message with utf-8 encode, to the server.
        rec_data = socket_obj.recv(1024).decode('utf-8')    # Received data from the server.
        print(rec_data)     # Print the received data form the server.
        msg = input()       # Typing the new message for the server.
        socket_obj.close()

if __name__ == "__main__":

    main()
