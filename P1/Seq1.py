class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq Created")
            return
        for i in strbases:
            if i not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR"
                print("INVALID Seq")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        counter = 0
        if self.strbases == self.NULL:
            return counter
        elif self.strbases == "ERROR":
            return counter
        else:
            return len(self.strbases)

    def count_base(self, base):
        counter = 0
        if self.strbases == self.NULL:
            return counter
        elif self.strbases == "ERROR":
            return counter
        else:
            for element in self.strbases:
                if element == base:
                    counter = counter + 1
            return counter, round((counter/self.len())*100, 1)

    def count(self):
        if self.strbases == self.NULL:
            d = {"A": 0, "T": 0, "C": 0, "G": 0}
        elif self.strbases == "ERROR":
            d = {"A": 0, "T": 0, "C": 0, "G": 0}
        else:
            d = {"A": 0, "T": 0, "C": 0, "G": 0}
            for element in self.strbases:
                if element == "A":
                    d["A"] += 1
                elif element == "C":
                    d["C"] += 1
                elif element == "G":
                    d["G"] += 1
                else:
                    d["T"] += 1
        return d

    def reverse(self):
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases
        else:
            d = {"A": "T", "T": "A", "C": "G", "G": "C"}
            value = ""
            for element in self.strbases:
                value = value + d[element]
            return value

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        content = file_contents.split("\n")[1:]
        self.strbases = "".join(content)
        return self

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
