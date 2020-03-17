import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8086

sequence_list = ["AGTG\n", "CATG\n", "TATGG\n", "GAATG\n", "ACTG\n"]
list_bases = ["A", "T", "C", "G"]
s1 = Seq()
folder = "../Session-04/"
EXT = ".txt"


# --- Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 3: Only on servers, convert into a listening socket
ls.listen()

print("SEQ Server configured")

while True:
    try:
        # --- Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()
        print("Waiting for clients...")

    except KeyboardInterrupt:
        print("Server is done")
        ls.close()
        exit()
    else:
        # --- Step 5: Receiving information for the client. First receiving a raw of bytes (max) and decode it into txt
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: {msg}")

        if msg == "PING":
            termcolor.cprint("PING command", "green")

        # --- Step 6: Send a response message to the client
            response = "OK!\n"
            cs.send(response.encode())
            print(response)

        elif msg.startswith("GET"):
            termcolor.cprint("GET", "green")
            index = 0
            for i in sequence_list:
                if msg[4] == str(index):
                    cs.send(i.encode())
                    print(i)
                index += 1

        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            sequence = Seq(msg[5:])
            print(f"Sequence: {sequence}")
            cs.send(str(sequence).encode())
            print(f"Total lenght: {sequence.len()}")
            for base in list_bases:
                print(f"{base}: {sequence.count_base(base)[0]} ({sequence.count_base(base)[1]}%)", end= "\n")

        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", "green")
            sequence = Seq(msg[5:])
            print(sequence.complement())
            cs.send(str(sequence.complement()).encode())

        elif msg.startswith("REV"):
            termcolor.cprint("REV", "green")
            sequence = Seq(msg[4:])
            print(sequence.reverse())
            cs.send(str(sequence.reverse()).encode())

        elif msg.startswith("GENE"):
            termcolor.cprint("GENE", "green")
            sequence = str(msg[5:])
            gene = s1.read_fasta(folder + sequence + EXT)
            print(gene)
            cs.send(str(gene).encode())

        cs.close()
