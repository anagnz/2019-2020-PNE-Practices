import pathlib
import http.server
import socketserver
import termcolor


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read(filename):
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        FOLDER1 = "../P4/"
        FOLDER2 = "../Session-14"

        req_line = self.requestline.split()

        if req_line[1] == "/" or req_line[1] == "/index.html":
            FILENAME = "Index.html"
            contents= read(FOLDER2 + FILENAME)
            self.send_response(200)

        else:
            FILENAME = "Error.html"
            contents = read(FOLDER1 + FILENAME)
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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
