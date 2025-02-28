import socketserver
from Protocol.FileSearchProtocol import FileSearchProtocol

def run():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), FileSearchProtocol) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()