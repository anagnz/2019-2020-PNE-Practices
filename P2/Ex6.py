from Seq1 import Seq

from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
s1 = Seq()
folder = "../Session-04/"
EXT = ".txt"
sequence = s1.read_fasta(folder + "FRAT1" + EXT)


print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")

c.talk("Sending FRAT1 Gene to the Server in fragments of 10 bases...")
c.talk(str(sequence))
print(f"Gene FRAT1: {str(sequence)}")

c.talk(str(sequence)[0:10])
print(f"Fragment 1: {str(sequence)[0:10]}")

c.talk(str(sequence)[10:20])
print(f"Fragment 2: {str(sequence)[10:20]}")

c.talk(str(sequence)[20:30])
print(f"Fragment 3: {str(sequence)[20:30]}")

c.talk(str(sequence)[30:40])
print(f"Fragment 4: {str(sequence)[30:40]}")

c.talk(str(sequence)[40:50])
print(f"Fragment 5: {str(sequence)[40:50]}")
