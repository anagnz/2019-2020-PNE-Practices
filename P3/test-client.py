from Seq1 import Seq

from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

sequence_list = ["AGTG\n", "CATG\n", "TATGG\n", "GAATG\n", "ACTG\n"]

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8086

# -- Create a client object
c = Client(IP, PORT)

print(f"* Testing PING...")
print(c.talk("PING"))

print(f"* Testing GET...")
print("GET 1: ", c.talk("GET 1"))
print("GET 2: ", c.talk("GET 2"))
print("GET 3: ", c.talk("GET 3"))
print("GET 4: ", c.talk("GET 4"))

print(f"* Testing INFO...")
print(c.talk("INFO AGAGAGATTTCC"))

print(f"* Testing COMP...")
print("COMP", c.talk("COMP AGATCCAT"))

print(f"* Testing REV...")
print("REV", c.talk("REV AGATCCAT"))

print(f"* Testing GENE...")
print("GENE U5", c.talk("GENE U5"))
print("GENE FRAT1", c.talk("GENE FRAT1"))
print("GENE ADA", c.talk("GENE ADA"))
print("GENE FXN", c.talk("GENE FXN"))
print("GENE RNU6_269P", c.talk("GENE RNU6_269P"))
