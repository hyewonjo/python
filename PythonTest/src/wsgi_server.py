'''
Created on 2018. 5. 29.

@author: hyewonj
'''
from wsgiref.simple_server import make_server #wsgiref.simple_server 모듈의 make_server 클래스르 가져온다.

def application(environ, start_response):
    response_body = ['%s: %s' % (key, value)
                     for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain; charset=utf-8'), ('Content-Length', str(len(response_body)))]
    
    start_response(status, response_headers)
    
    return[response_body.encode("utf-8")]
    
httpd = make_server('localhost', 8051, application)

httpd.handle_request()