import socket

HOST = 'localhost'
PORTA = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORTA))
s.sendall(str.encode('Curso de Redes.'))
dados = s.recv(1024)

print('Mensagem recebida:', dados.decode())