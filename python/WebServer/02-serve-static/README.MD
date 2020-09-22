python 3 接口有变：
1. BaseHTTPServer  ->  http.server
2. 写的数据应该是byte


*   Use BaseHTTPServer to handle socket connections and parse HTTP requests.
*   Respond to GET requests with information about the request.
*   To test:
    *   Run `python server.py`.
    *   Point browser at `http://localhost:port/something/or/other`
    
    
