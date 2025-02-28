import os
from datetime import datetime

def search_files(fragment):
    result = []
    drives = ['C:', 'D:', 'E:', 'F:'] 

    for drive in drives:
        for root, dirs, files in os.walk(drive):
            for file in files:
                if fragment in file:
                    file_path = os.path.join(root, file)
                    try:
                        stats = os.stat(file_path)
                        file_info = {
                            "FileName": file,
                            "FullPath": file_path,
                            "SizeBytes": stats.st_size,
                            "CreationDate": datetime.fromtimestamp(stats.st_ctime).isoformat()
                        }
                        result.append(file_info)
                    except PermissionError:
                        continue  

    return result