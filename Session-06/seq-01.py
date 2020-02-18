class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases): #strbases is a parameter that
        self.strbases = strbases # 1 st strbases is a variable
        print("New sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    pass


# .. Main program
s1 = Seq("AACGTC")
g = Gene("ACCTGA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {g}")
l1 = s1.len()
print(f"The lenght of the first sequence is {l1}")
print(f"The lenght of the second sequence is {g.len()}")

