from Seq0 import *

folder = "../Session-04/"
txt = ".txt"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for element in list_genes:
    dna_seq = seq_read_fasta(folder + element + txt)
    print("Gene", element, "---> length:", seq_len(dna_seq))
