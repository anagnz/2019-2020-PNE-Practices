import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080

sequence_list = ["AGTG\n", "CATG\n", "TATGG\n", "GAATG\n", "ACTG\n"]
Folder = "../Session-04/"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split()[1]

        init = req_line.split("?")[0]

        if init == "/":
            contents = Path('main-page.html').read_text()
            self.send_response(200)
        elif init == "/ping":
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>PING</title>
                          </head>
                          <body>
                            <h2>PING OK!</h2>
                            <p>The SEQ2 server is running </p>  
                            <p><p>
                            <a href="http://127.0.0.1:8080/">Main page</a>
                            </form>
                          </body>
                        </html>
                        """
            self.send_response(200)
        elif init == "/get":
            value = req_line.split("=")[1]
            number = int(value)
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>GET</title>
                          </head>
                          <h2>Sequence number {number} </h2>  
                          <body>
                            <p>{sequence_list[number]}</p>  
                            <p><p>
                            <a href="http://127.0.0.1:8080/">Main page</a>
                          </body>
                        </html>
                        """
            self.send_response(200)
        elif init == "/gene":
            value = req_line.split("=")[1]
            gene = Seq()
            sequence = gene.read_fasta(Folder + value + ".txt")
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>GET</title>
                          </head>
                          <h2>Gene: {value} </h2>  
                          <body>
                            <textarea readonly rows="20" cols="80">{sequence} </textarea>  
                            <br>
                            <a href="http://127.0.0.1:8080/">Main page</a>
                          </body>
                        </html>
                        """
            self.send_response(200)
        elif init == "/operation":
            value = req_line.split("?")[1]
            values = value.split("&")
            name_seq = values[0].split("=")[1]
            operation = values[1].split("=")[1]
            sequence = Seq(name_seq)
            print(name_seq)
            if operation == "Rev":
                result = sequence.reverse()
            elif operation == "Comp":
                result = sequence.complement()
            elif operation == "Info":
                total_lenght = sequence.len()
                counter_A = sequence.count_base("A")
                counter_C = sequence.count_base("C")
                counter_G = sequence.count_base("G")
                counter_T = sequence.count_base("T")

                result = f"""
                <p>Total lenght: {total_lenght}<p>
                <p>A: {counter_A[0]} ({counter_A[1]})%<p>
                <p>C: {counter_C[0]} ({counter_C[1]})%<p>
                <p>G: {counter_G[0]} ({counter_G[1]})%<p>
                <p>T: {counter_T[0]} ({counter_T[1]})%<p>
                 """

            contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>OPERATION</title>
                      </head>
                      <h2>Sequence</h2>  
                      <p>{name_seq}<p>  
                      <h2>Operation: </h2>  
                      <p>{operation}<p>
                      <h2>Result: </h2>  
                      <body>
                        <p>{result}</p>  
                        <br>
                        <a href="http://127.0.0.1:8080/">Main page</a>
                      </body>
                    </html>
                    """
            self.send_response(200)
        else:
            contents = Path('error.html').read_text()
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()