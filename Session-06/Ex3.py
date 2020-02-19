class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        for i in strbases:
            if i not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR!!"
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

# ..Main program


def print_seqs(seq_list):
    index = 0
    for element in seq_list:
        print(f"Sequence {index}: (Lenght {element.len()}) {element}")
        index = index + 1


def generate_seqs(pattern, number):
    new_list = []
    for element in range(1, number+1):
        sequence = pattern * element
        new_list.append(Seq(sequence))
    return new_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
