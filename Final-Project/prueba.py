import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq


list_bases = ["A", "C", "G", "T"]


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

        if init == "/":
            contents = Path('main-page.html').read_text()
            type = 'text/html'
            self.send_response(200)

        elif init == "/listSpecies":
            parameters = req_line.split("?")[1]
            values = parameters.split("&")
            info = get_info("info/species?")["species"]

            if len(values) == 2:
                input, json = values
                limit = input.split("=")[1]
                counter = 0
                if json == "json=1":
                    if 267 > int(limit):
                        species_dict = {}
                        for element in info:
                            species_dict.update({counter: element["display_name"]})
                            counter += 1
                    data = {'ListSpecies': species_dict}
                    contents = json.dumps(data)
                    self.response(200)
                    type = 'application/json'

                else:
                    contents = Path('error.html').read_text()
                    self.send_response(404)

            elif len(values) == 1:
                type = 'text/html'
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
            type = 'text/html'
            specie = req_line.split("=")[1]
            info = get_info("info/assembly/" + specie + "?")["karyotype"]
            contents = html("KARYOTYPE OF A SPECIFIC SPECIES", "lightblue")
            contents += f"""<h> The names of the chromosomes are: </h>"""
            for element in info:
                contents = contents + f"""<p> • {element}</p>"""
            self.send_response(200)
        elif init == "/chromosomeLength":
            type = 'text/html'
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
            type = 'text/html'
            gene = req_line.split("=")[1]
            gene_id = get_info(f"/xrefs/symbol/homo_sapiens/{gene}?")[0]["id"]
            info = get_info(f"/sequence/id/{gene_id}?")
            contents = html("GENE SEQUENCE", "lightyellow")
            contents += f'<p> The sequence of gene {gene} is: </p>'
            contents += f'<textarea rows = "100" "cols = 500"> {info["seq"]} </textarea>'
            self.send_response(200)
        elif init == "/geneInfo":
            type = 'text/html'
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
            type = 'text/html'
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
            type = 'text/html'
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