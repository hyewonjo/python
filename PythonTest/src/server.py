'''
Created on 2018. 5. 29.

@author: hyewonj
'''
import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
#socketserver모듈의 TCPServer 클래스를 인스턴스화 하고, PORT
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

