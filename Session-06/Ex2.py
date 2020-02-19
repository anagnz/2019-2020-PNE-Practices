class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    index = 0
    for element in seq_list:
        print(f"Sequence {index}: (Lenght {element.len()}) {element}")
        index = index + 1


seq_lists = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_lists)
