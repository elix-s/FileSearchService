from Model.FileSearchModel import FileSearchModel

class FileSearchContext:
    def __init__(self):
        self.query = ""
        self.results = []

    def process_query(self, query):
        self.query = query
        self.results = FileSearchModel.search_files(query)