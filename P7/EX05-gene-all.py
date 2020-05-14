from Seq1 import Seq
import http.client
import json
import termcolor

dict_genes = {
    'FRAT1': "ENSG00000165879",
    'ADA': "ENSG00000196839",
    'FXN': "ENSG00000165060",
    'RNU6_269P': "ENSG00000212379",
    'MIR633': "ENSG00000207552",
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

list_bases = ["A", "C", "G", "T"]


for element in dict_genes:

    SERVER = 'rest.ensembl.org'
    endpoint = "/sequence/id/"
    gene_id = dict_genes[element]
    parameters = "?content-type=application/json"
    URL = SERVER + endpoint + gene_id + parameters

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", "/" + endpoint + gene_id + parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    response = json.loads(data1)

    termcolor.cprint(f"Gene: ", "green", end="")
    print(element)
    termcolor.cprint(f"Description: ", "green", end="")
    print(response['desc'])

    bases = response['seq']

    sequence = Seq(bases)

    termcolor.cprint(f"Total lengh: ", "green", end="")
    print(sequence.len())

    freq_counter = 0

    for base in list_bases:
        sequence.count_base(base)
        termcolor.cprint(f"{base}: ", "blue", end="")
        print(f"{sequence.count_base(base)[0]} ({sequence.count_base(base)[1]}%)")
        if sequence.count_base(base)[0] > freq_counter:
            freq_counter = sequence.count_base(base)[0]
            freq_base = base

    termcolor.cprint(f"Most frequent Base: ", "green", end="")
    print(freq_base)
