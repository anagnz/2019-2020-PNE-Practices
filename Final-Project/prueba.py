import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq


list_bases = ["A", "C", "G", "T"]


def dict_listSpecies(limit, list):
    contents = {
        "Total number of species": 267,
        "Limit selected": limit,
        "List of species": list
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_karyotype(list):
    contents = {
        "The names of the chromosomes are": list
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_chromosomeLength(length):
    contents = {
        "The length of the selected chromosome is": length
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneSeq(seq):
    contents = {
        "The sequence of the selected gen is": seq
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneInfo(start, end, length, id, chromo): #no me sale :(
    contents = {
        "The start point is": start,
        "The end point is": end,
        "The length of the gene is": length,
        "The ID of the gene is": id,
        "The chromosome of this gene is": chromo
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneCalc(length, calc_A, calc_C, calc_G, calc_T):
    contents = {
        "Total length of the gene is": length,
        "The percentage of each base in the sequence of this gene is"
        "A": calc_A,
        "C": calc_C,
        "G": calc_G,
        "T": calc_T
    }
    client_dict = json.dumps(contents)
    return client_dict

def dict_geneList(list):
    contents = {
        "List of genes located in the introduced chromosome": list
    }
    client_dict = json.dumps(contents)
    return client_dict

def html(title, color):
    return f"""
                <!DOCTYPE html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>{title}</title>
                  </head>
                  <body style="background-color: {color}">
                    <p><p>
                    </form>
                  </body>
                </html>
                """


def get_info(endpoint):

    port = 8080
    server = 'rest.ensembl.org'
    parameters = "content-type=application/json"
    print(f"\nConnecting to server: {server}:{port}\n")

    conn = http.client.HTTPConnection(server)

    try:
        conn.request("GET", endpoint+parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    return response


port = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split()[1]
        init = req_line.split("?")[0]

        try:
            if init == "/":
                contents = Path('main-page.html').read_text()
                self.send_response(200)

            elif init == "/listSpecies":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")
                info = get_info("info/species?")["species"]

                if len(values) == 2:
                    input, json = values
                    limit = input.split("=")[1]
                    if json == "json=1":
                        list = []
                        counter = 0
                        if 267 > int(limit):
                            for element in info:
                                if counter < int(limit):
                                    list.append(element["display_name"])
                                    counter += 1
                            contents = dict_listSpecies(limit, list)
                        elif limit == " " :
                            for element in info:
                                list.append(element["display_name"])
                                counter += 1
                            contents = dict_listSpecies(limit, list)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 1:
                    limit = req_line.split("=")[1]
                    contents = html("LIST OF SPECIES IN THE BROWSER", "lightblue")
                    contents += f"""<h>The total number of species in ensembl is: 267</h><br>"""
                    contents += f"""<h>The limit you have selected is: {limit}</h><br>"""
                    contents += f"""<h>The names of the species are:</h>"""
                    if limit == "":
                        for element in info:
                            contents += f"""<p> • {element["display_name"]}</p>"""
                    elif 267 >= int(limit):
                        counter = 0
                        for element in info:
                            if counter < int(limit):
                                contents += f"""<p> • {element["display_name"]}</p>"""
                                counter += 1
                    else:
                        for element in info:
                            contents += f"""<p> • {element["display_name"]}</p>"""
                self.send_response(200)

            elif init == "/karyotype":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 2:
                    input, json = values
                    specie = input.split("=")[1]
                    info = get_info("info/assembly/" + specie + "?")["karyotype"]
                    if json == "json=1":
                        list = []
                        for element in info:
                            list.append(element)
                        contents = dict_karyotype(list)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)
                elif len(values) == 1:
                    specie = req_line.split("=")[1]
                    info = get_info("info/assembly/" + specie + "?")["karyotype"]
                    contents = html("KARYOTYPE OF A SPECIFIC SPECIES", "lightblue")
                    contents += f"""<h> The names of the chromosomes are: </h>"""
                    for element in info:
                        contents = contents + f"""<p> • {element}</p>"""
                self.send_response(200)

            elif init == "/chromosomeLength":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 3:
                    input1, input2, json = values
                    specie = input1.split("=")[1]
                    chromo = input2.split("=")[1]
                    info = get_info(f"info/assembly/" + specie + "?")["top_level_region"]

                    if json == "json=1":
                        for element in info:
                            if element["name"] == chromo:
                                length = element["length"]
                        contents = dict_chromosomeLength(length)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 2:
                    number = req_line.split("=")[2]
                    values = req_line.split("=")[1]
                    specie = values.split("&")[0]
                    info = get_info(f"info/assembly/" + specie + "?")["top_level_region"]
                    for element in info:
                        if element["name"] == number:
                            contents = html("LENGTH OF THE CHROMOSOME SELECTED", "lightblue")
                            contents += f"""<h> The length of the chromosome is: {element["length"]}</h>"""
                    self.send_response(200)

            elif init == "/geneSeq":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 2:
                    input, json = values
                    gene = input.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/sequence/id/{gene_id}?")

                    if json == "json=1":
                        contents = dict_geneSeq(info["seq"])
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 1:
                    gene = req_line.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/sequence/id/{gene_id}?")
                    contents = html("GENE SEQUENCE", "lightyellow")
                    contents += f'<p> The sequence of gene {gene} is: </p>'
                    contents += f'<textarea rows = "100" "cols = 500"> {info["seq"]} </textarea>'
                self.send_response(200)

            elif init == "/geneInfo":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 2:
                    input, json = values
                    gene = input.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/sequence/id/{gene_id}?")

                    if json == "json=1":
                        length = info["end"] - info["start"]
                        contents = dict_geneInfo(info["start"], info["end"], length, info["id"], info["seq_region_name"])
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 1:
                    gene = req_line.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/lookup/id/{gene_id}?")
                    contents = html("INFO ABOUT A GENE", "lightyellow")
                    contents += f'<h1> Information about the introduced gene: {gene}</h1>'
                    contents += f'<p> The start point is: {info["start"]}</p>'
                    contents += f'<p> The end point is: {info["end"]}</p>'
                    contents += f'<p> The length of the gene is: {info["end"]-info["start"]}</p>'
                    contents += f'<p> The id of the gene is: {info["id"]}</p>'
                    contents += f'<p> The chromosome of that gene is: {info["seq_region_name"]}</p>'
                self.send_response(200)

            elif init == "/geneCalc":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 2:
                    input, json = values
                    gene = input.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/sequence/id/{gene_id}?")["seq"]
                    sequence = Seq(info)
                    if json == "json=1":
                        dict = {}
                        for base in list_bases:
                            dict.update(f"{base}: ({sequence.count_base(base)[1]}%)")
                        contents = dict_geneCalc(sequence.len(), dict)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 1:
                    gene = req_line.split("=")[1]
                    gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
                    info = get_info(f"/sequence/id/{gene_id}?")["seq"]
                    sequence = Seq(info)
                    contents = html("BASES CALCULATION", "lightyellow")
                    contents += f'<h1> Calculations over the introduced gene: {gene}</h1>'
                    contents += f'<p> Total length of this gene is: {sequence.len()}</p>'
                    contents += f'<p> The percentage of each base in the sequence of this gene is:</p>'
                    for base in list_bases:
                        contents += f"<p>{base}: ({sequence.count_base(base)[1]}%)</p>"
                self.send_response(200)

            elif init == "/geneList":
                parameters = req_line.split("?")[1]
                values = parameters.split("&")

                if len(values) == 4:
                    input1, input2, input3, json = values
                    chromo = input1.split("=")[1]
                    start = input2.split("=")[1]
                    end = input3.split("=")[1]
                    info = get_info(f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene;")

                    if json == "json=1":
                        list = []
                        for element in info:
                            list.append(element["external_name"])
                        contents = dict_geneList(list)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)

                elif len(values) == 3:
                    values = req_line.split("?")[1]
                    chromo, start, end = values.split("&")
                    chromo_value = chromo.split("=")[1]
                    start_value = start.split("=")[1]
                    end_value = end.split("=")[1]
                    info = get_info(f"/overlap/region/human/{chromo_value}:{start_value}-{end_value}?feature=gene;")
                    contents = html("LIST OF GENES OF A CHROMOSOME", "lightyellow")
                    contents += f'<h2> List of genes located in the introduced chromosome: {chromo_value}</h2>'
                    for element in info:
                        contents += f'<p>- {element["external_name"]}</p>'
                self.send_response(200)
            else:
                contents = Path('error.html').read_text()
                self.send_response(404)

        except (KeyError, TypeError, ValueError, IndexError):
            contents = Path('error.html').read_text()
            self.send_response(200)

        endpoints = ["/", "/listSpecies", "/karyotype", "/chromosomeLength",
                          "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]

        if init in endpoints: #esto hay que cambiarlo pero no se como llegar al siguiente if sino :))
            if "json=1" in req_line:
                type = "application/json"
            else:
                type = "text/html"
            self.send_header('Content-Type', type)
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:

    print("Serving at PORT", port)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")

        httpd.server_close()
