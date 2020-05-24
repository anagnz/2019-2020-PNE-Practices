import http.client
import termcolor
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
    8.- Finish
    """)


def client(client_request):
    port = 8080
    server = 'localhost'
    print(f"\nConnecting to server: {server}:{port}\n")
    conn = http.client.HTTPConnection(server, port)
    
    try:
        conn.request("GET", client_request + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data = json.loads(data1)
    print(f"CONTENT: {data}")

valid = True
while valid:
    menu()
    options = int(input("Choose an option: "))

    if options == 1:
        limit = input("Type the number of species you want to be shown: ")
        url = "/listSpecies?limit=" + limit
        client(url)
