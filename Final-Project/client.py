import http.client
import json


def menu():
    print("""
    1.- /listSpecies
    2.- /karyotype
    3.- /chromosomeLength
    4.- /geneSeq
    5.- /geneInfo
    6.- /geneCalc
    7.- /geneList
    8.- Finish the loop
    """)


def client(client_request, json_param):
    port = 8080
    server = 'localhost'
    print(f"\nConnecting to server: {server}:{port}\n")
    conn = http.client.HTTPConnection(server, port)

    try:
        conn.request("GET", client_request + "&json=" + json_param)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data = json.loads(data1)
    print(data)


valid = True
while valid:
    menu()
    json_param = input("Choose a json parameter(must be 1 for it to work): ")
    options = int(input("Choose an option: "))

    if options == 1:
        limit = input("Type the number of species you want to be shown: ")
        url = "/listSpecies?limit=" + limit
        client(url, json_param)

    elif options == 2:
        specie = input("Choose any specie: ")
        url = "/karyotype?specie=" + specie
        client(url, json_param)

    elif options == 3:
        specie = input("Choose specie: ")
        chromosome = input("Choose chromosome: ")
        url = f"/chromosomeLength?specie={specie}&chromo={chromosome}"
        client(url, json_param)
    elif options == 4:
        gene = input("Choose a human gene: ")
        url = "/geneSeq?gene=" + gene
        client(url, json_param)

    elif options == 5:
        gene = input("Choose a human gene: ")
        url = "/geneInfo?gene=" + gene
        client(url, json_param)

    elif options == 6:
        gene = input("Choose a human gene: ")
        url = "/geneCalc?gene=" + gene
        client(url, json_param)

    elif options == 7:
        chromo = input("Choose a human chromosome: ")
        start = input("Choose the start point: ")
        end = input("Choose the end point: ")
        url = f"/geneList?chromo={chromo}&start={start}&end={end}"
        client(url, json_param)

    elif options == 8:
        valid = False
    else:
        print("Choose a valid option between 1-8")
