# -*- coding: utf-8 -*-
"""
   File Name：     BaseServer
   Author :       jing
   Date：          2020/4/27
   基于python库，自写一个web server，响应访问
"""

import http.server as BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Handle HTTP requests by returning a fixed 'page'."""
    # Page to send back.
    Page = '''\
    <html>
    <body>
    <p>Hello, web!</p>
    </body>
    </html>
    '''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf8'))


# ----------------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('127.0.0.1', 8889)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()


