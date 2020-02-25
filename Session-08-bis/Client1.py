import socket


# --The IP of the server we want to connect to
IP = "212.128.253.128"
PORT = 8080
Max_requests = 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1 socket is the module and the 2 is the type, we'll always use the same type


# --Establishing the connection with the server
s.connect((IP, PORT))


# sockets only know how to send bytes not strings so we have to convert it --Send data to the server
s.send(str.encode("hello"))

# --Receive data from the server
# --(number of bytes received)
msg = s.recv(2048)

print("Message from the server: ", msg.decode("utf-8"))

# --Closing the connection
s.close()
