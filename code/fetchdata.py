import socket

host = "data.pr4e.org"
port = 80
request = f"GET /intro-short.txt HTTP/1.0\r\nHost: {host}\r\n\r\n"

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(request.encode())

# Receive response
response = sock.recv(4096).decode()
sock.close()

# Print the HTTP response headers
headers = response.split("\r\n\r\n")[0]  # Split headers from body
print(headers)
