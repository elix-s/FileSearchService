from Model.FileSearchModel import search_files

class SearchContext:
    def __init__(self):
        self.query = ""
        self.results = []

    def process_query(self, query):
        self.query = query
        self.results = search_files(query)