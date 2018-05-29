'''
Created on 2018. 5. 29.

@author: hyewonj
'''
import http.server
import socketserver

PORT = 8080

Handler = http.server.CGIHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.server_name = "localhost"
httpd.server_port = PORT

httpd.serve_forever()