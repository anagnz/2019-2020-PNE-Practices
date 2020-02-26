from Seq1 import *

folder = "../Session-04/"
EXT = ".txt"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Practice 1, Exercise 9 |------")

for element in list_genes:
    s = Seq()
    dna_seq = s.read_fasta(folder + element + EXT)
    dict_bases = s.count()
    min_value = 0
    most_frc_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            most_frc_base = base

    print("Gene", element, ": Most frecuent Base: ", most_frc_base)