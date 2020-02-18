from Seq0 import *

folder = "../Session-04/"
filename = "U5.txt"

print("-----| Exercise 7 |------")
print("Gene U5: ")
print("Frag: ", seq_read_fasta(folder+filename)[0:20])
print("Comp: ", seq_complement(seq_read_fasta(folder+filename)[0:20]))