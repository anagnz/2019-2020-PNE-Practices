from Seq0 import *

folder = "../Session-04/"
txt = ".txt"
list_bases = ["A", "C", "T", "G"]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 4 |------")
for element in list_genes:
    dna_seq = seq_read_fasta(folder + element + txt)
    print("Gene", element)
    for base in list_bases:
        print(base, ":", seq_count_base(dna_seq, base))
