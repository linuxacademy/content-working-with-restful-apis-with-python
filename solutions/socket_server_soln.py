import http.server


class PostHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):

        # print(self.__dict__)

        data = self.rfile.read(int(self.headers["Content-Length"]))

        self.send_response(201)
        self.wfile.write(b"Hello Cloud Guru " + data + b". I am very glad you are here.")

if __name__ == '__main__':
    PORT = 57392
    server = http.server.HTTPServer(('', PORT), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()


