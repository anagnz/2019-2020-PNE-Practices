from Seq1 import *

print("-----| Practice 1, Exercise 7 |------")

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")


print(f"Sequence 1: (Lenght {s1.len()}) {s1}")
print(f"    Bases: {s1.count()}")
print(f"    Rev: {s1.reverse()}")
print(f"Sequence 2: (Lenght {s2.len()}) {s2}")
print(f"    Bases: {s2.count()}")
print(f"    Rev: {s2.reverse()}")
print(f"Sequence 3: (Lenght {s3.len()}) {s3}")
print(f"    Bases: {s3.count()}")
print(f"    Rev: {s3.reverse()}")