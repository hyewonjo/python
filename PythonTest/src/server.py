'''
Created on 2018. 5. 29.

@author: hyewonj
'''
import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
#socketserver모듈의 TCPServer 클래스를 인스턴스화 하고, PORT로 들어오는 요청을 http.server 모듈의 SimpleHTTPRequestHandler가 처리할 것임을 알려줌.
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)

#소켓 서버가 PORT로 들어오는 연결을 계속해서 감시하도록 하는 데 사용 
httpd.serve_forever()