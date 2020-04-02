import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
endpoint = "/sequence/id"
gene_id = "/ENSG00000207552"
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
    conn.request("GET", "/"+endpoint+gene_id+parameters)
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
print("MIR633")
termcolor.cprint(f"Description: ", "green", end="")
print(response['desc'])
termcolor.cprint(f"Bases:" , "green", end="")
print(response['seq'])

