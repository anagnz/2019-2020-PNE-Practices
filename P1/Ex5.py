from Seq1 import *

print("-----| Practice 1, Exercise 5 |------")

list_bases = ["A", "T", "C", "G"]

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Lenght {s1.len()}) {s1}")
for base in list_bases:
    print(base, ":",  s1.count_base(base), end = ", ")
print()
print(f"Sequence 2: (Lenght {s2.len()}) {s2}")
for base in list_bases:
    print(base, ":",  s2.count_base(base), end = ", ")
print()
print(f"Sequence 3: (Lenght {s3.len()}) {s3}")
for base in list_bases:
    print(base, ":",  s3.count_base(base), end = ", ")