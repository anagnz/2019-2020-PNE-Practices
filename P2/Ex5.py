from Seq1 import Seq

from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
s1 = Seq()
folder = "../Session-04/"
EXT = ".txt"
sequence = s1.read_fasta(folder+"U5"+EXT)


print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
c.debug_talk("Sending the U5 Gene to the server...")
c.debug_talk(str(sequence))
