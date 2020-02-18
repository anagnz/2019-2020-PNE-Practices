def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()

    content = file_contents.split("\n")[1:]
    body_file = ",".join(content).replace(",", "")
    return body_file


def seq_len(seq):
    count = 0
    for i in seq:
        count = count + 1
    return count


def seq_count_base(seq, base):
    counter = 0
    for element in seq:
        if element == base:
            counter = counter + 1
    return counter


def seq_count(seq):
    d = {"A": 0, "T": 0, "C": 0, "G": 0}
    for element in seq:
        if element == "A":
            d["A"] += 1
        elif element == "C":
            d["C"] += 1
        elif element == "G":
            d["G"] += 1
        else:
            d["T"] += 1
    return d


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(seq):
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}

    value = ""

    for element in seq:
        value = value + d[element]

    return value