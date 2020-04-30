import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json


port = 8080

socketserver.TCPServer.allow_reuse_address = True


def get_info(endpoint):

    port = 8080
    server = 'rest.ensembl.org'
    parameters = "?content-type=application/json"
    print(f"\nConnecting to server: {server}:{port}\n")

    # Connect with the server
    conn = http.client.HTTPConnection(server)

    try:
        conn.request("GET", endpoint+parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    # we change the format of the info to JSON format
    response = json.loads(data1)
    return response


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split()[1]
        init = req_line.split("?")[0]

        if init == "/":
            contents = Path('main-page.html').read_text()
            self.send_response(200)
        elif init == "/listSpecies":
            limit = req_line.split("=")[1]
            info = get_info("info/species")["species"]
            if limit == "":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <title>LIST OF SPECIES IN THE BROWSER</title>
                              </head>
                              <body style="background-color: lightblue">
                                <h>The total number of species in ensembl is: 267</h><br>
                                <h>The limit you have selected is: {limit}</h>
                                <p><p>
                                </form>
                              </body>
                            </html>
                            """
                for element in info:
                    contents = contents + f"""<p> • {element["common_name"]}</p>"""

            if 267 >= int(limit):
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <title>LIST OF SPECIES IN THE BROWSER</title>
                              </head>
                              <body style="background-color: lightblue">
                                <h>The total number of species in ensembl is: 267</h><br>
                                <h>The limit you have selected is: {limit}</h>
                                <p><p>
                                </form>
                              </body>
                            </html>
                            """
                counter = 0
                for element in info:
                    if counter < int(limit):
                        contents = contents + f"""<p> • {element["common_name"]}</p>"""
                        counter = counter + 1
            else:
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <title>LIST OF SPECIES IN THE BROWSER</title>
                              </head>
                              <body style="background-color: lightblue">
                                <h>The total number of species in ensembl is: 267</h><br>
                                <h>The limit you have selected is: {limit}</h>
                                <p><p>
                                </form>
                              </body>
                            </html>
                            """
                for element in info:
                    contents = contents + f"""<p> • {element["common_name"]}</p>"""
            self.send_response(200)
        elif init == "/karyotype":
            contents = get_info("")
            self.send_response(200)
        elif init == "/chromosomeLength":
            contents = get_info("")
            self.send_response(200)
        else:
            contents = Path('error.html').read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", port), Handler) as httpd:

    print("Serving at PORT", port)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")

        httpd.server_close()
