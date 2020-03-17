from Seq1 import Seq

from Client0 import Client

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT_1 = 8080
PORT_2 = 8081

# -- Create a client object
c1 = Client(IP, PORT_1)
c2 = Client(IP, PORT_2)
s1 = Seq()
folder = "../Session-04/"
EXT = ".txt"
sequence = s1.read_fasta(folder + "FRAT1" + EXT)


print(f"Connection to SERVER 1 at {c1.ip}, PORT: {c1.port}")
print(f"Connection to SERVER 2 at {c2.ip}, PORT: {c2.port}")
c1.talk("Sending FRAT1 Gene to the Server in fragments of 10 bases...")
c2.talk("Sending FRAT1 Gene to the Server in fragments of 10 bases...")
print(f"Gene FRAT1: {str(sequence)}")

# ---Creating fragments
Fragment_1 = str(sequence)[0:10]
Fragment_2 = str(sequence)[10:20]
Fragment_3 = str(sequence)[20:30]
Fragment_4 = str(sequence)[30:40]
Fragment_5 = str(sequence)[40:50]
Fragment_6 = str(sequence)[50:60]
Fragment_7 = str(sequence)[60:70]
Fragment_8 = str(sequence)[70:80]
Fragment_9 = str(sequence)[80:90]
Fragment_10 = str(sequence)[90:100]

list_fragments = [Fragment_1, Fragment_2, Fragment_3, Fragment_4, Fragment_5, Fragment_6, Fragment_7, Fragment_8, Fragment_9, Fragment_10]

# ---Printing them on the client's console
index = 0
for i in list_fragments:
    print(f"Fragment {index + 1}: {list_fragments[index]}")
    index += 1

# ---Sending them to the server's console

i = 0
for element in list_fragments:
    if i % 2 == 0 or i == 0:
        c1.talk(f"Fragment {i+1}: {list_fragments[i]}")
    elif i != 0:
        c2.talk(f"Fragment {i+1}: {list_fragments[i]}")

    i += 1
