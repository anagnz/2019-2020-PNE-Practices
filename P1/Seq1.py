class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        for i in strbases:
            if strbases == :
                self.strbases = "NULL"
                print("NULL Seq Created")
                return
            elif i not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR!!"
                print("Invalid Seq Created")
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
        index = index + 1
        print(f"Sequence {index}: (Lenght {element.len()}) {element}")


def generate_seqs(pattern, number):
    new_list = []
    for element in range(1, number+1):
        sequence = pattern * element
        new_list.append(Seq(sequence))
    return new_list
