import socket
import termcolor

IP = "212.128.253.140"
PORT = 8083

# --- Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- Step 3: Only on servers, convert into a listening socket
ls.listen()

print("Server is configured")

clients_list = []
connection_counter = 0
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
        connection_counter += 1
        print(f"CONNECTION {connection_counter}. Client IP, PORT: {client_ip_port}")
        clients_list.append(client_ip_port)
        # --- Step 5: Receiving information for the client. First receiving a raw of bytes (max) and decode it into txt
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: ", end = "")
        termcolor.cprint(msg, "green")

        # --- Step 6: Send a response message to the client
        response = f"ECHO: {msg}"
        cs. send(response.encode())

        if connection_counter == 5:
            print("The following clients has connected to the server: ")
            clients = 0
            for i in clients_list:
                print(f"Client {clients}: {clients_list[connection_counter-1]}")
                clients += 1
        cs.close()
