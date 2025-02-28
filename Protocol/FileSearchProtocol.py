import http.server
import urllib.parse
import json
from Context.FileSearchContext import SearchContext
from os import path

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.context = SearchContext()  
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.show_index_page()
        elif self.path.startswith('/search'):
            self.handle_search()
        else:
            super().do_GET()

    def handle_search(self):
        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        query = query_params.get('query', [''])[0] 
        if query:
            self.context.process_query(query)
        
        result = self.context.results
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        if result:
            self.wfile.write(json.dumps(result).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({"message": "No files found"}).encode('utf-8'))

    def show_index_page(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        with open(path.join('templates', 'index.html'), 'r', encoding='utf-8') as f:
            html = f.read()
        self.wfile.write(html.encode('utf-8'))