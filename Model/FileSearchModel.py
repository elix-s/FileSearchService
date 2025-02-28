import os
import string
from datetime import datetime

class FileSearchModel:
    def get_available_drives():
        drives = []
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drives.append(drive)
        return drives

    def search_files(fragment):
        result = []
        drives = FileSearchModel.get_available_drives()
        
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    file_path = os.path.join(root, file)
                    if fragment.lower() in file_path.lower():
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

