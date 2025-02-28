import socketserver
from Protocol.FileSearchProtocol import RequestHandler

def run():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()