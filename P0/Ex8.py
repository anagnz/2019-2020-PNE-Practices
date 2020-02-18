from Seq0 import *

folder = "../Session-04/"
txt = ".txt"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]

print("-----| Exercise 8 |------")

for element in list_genes:
    dna_seq = seq_read_fasta(folder + element + txt)
    dict_bases = seq_count(dna_seq)
    min_value = 0
    most_frc_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            most_frc_base = base

    print("Gene", element, ": Most frecuent Base: ", most_frc_base)
