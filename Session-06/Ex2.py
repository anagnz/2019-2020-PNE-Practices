class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases

    def print_seqs(self, list):
        index = 0
        for element in list:
            index = index +1
            print(element.len())
            print(element)


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

for element in seq_list:
    element.print_seqs()
