from Seq1 import *

FOLDER = "../Session-04/"
EXT = ".txt"

print("-----| Practice 1, Exercise 9 |------")

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FOLDER + "U5" + EXT)

print(f"Sequence : (Lenght {s.len()}) {s}")
print(f"    Bases: {s.count()}")
print(f"    Rev: {s.reverse()}")
print(f"    Comp: {s.complement()}")