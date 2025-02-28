# FileSearchService
Web-сервер для поиска файлов на компьютере на Windows по критерию вхождения строки в путь файла.<br>
Запуск - переходим в корень проекта и выполняем в консоли python server.py. Затем переходим на http://localhost:8000/ и вбиваем в поисковую форму нужную строку, по которой будет осуществляться поиск.<br>
Конфиг для запуска в Cline (конфиг также находится в корне проекта): <br>
{
    "FileSearchService": {
      "file-search-mcp": {
        "args": [
          "../FileSearchService/server.py"
        ],
        "command": "python",
        "autoApprove": [],
        "disabled": false
      }
    }
  }
