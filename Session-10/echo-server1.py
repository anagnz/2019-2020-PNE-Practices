import socket
import termcolor

IP = "212.128.253.140"
PORT = 8081

# --- Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- Step 3: Only on servers, convert into a listening socket
ls.listen()

print("Server is configured")

while True:
    print("Waiting for Clients to connect")

    try:
        # --- Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server is done")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        # --- Step 5: Receiving information for the client. First receiving a raw of bytes (max) and decode it into txt
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: ")
        termcolor.cprint(msg, "green")


        # --- Step 6: Send a response message to the client
        response = f"ECHO: {msg}"
        cs. send(response.encode())

        cs.close()
