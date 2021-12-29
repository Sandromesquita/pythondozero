# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:16:22 2021

@author: sandr
"""

import socket

"""
accept() - aceita a conexao
bind(endereco) - associa o socket servidor a um endereco
close() - fecha o socket
connect(endereco) - conecta um cliente a um endereco
listen() - comeca a escutar
recv(tamanho do pacote) - receber a mensagem
"""

#https://docs.python.org/pt-br/3.8/howto/sockets.html

HOST = 'localhost' #127.0.0.1
PORTA = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# FAMILIA DE ENDERECOS: AF_INET - endereco IPv4 / AF_INET6 - enedereco IPv6
# TIPO DE SOCKET: SOCK_STREAM - para socket TCP / SOCK_DGRAM - para socket UDP

s.bind((HOST, PORTA))
s.listen()

print("Aguardando um cliente se conectar...")

conectado, endereco = s.accept()

print("Conectado no endereco:", endereco)

while True:
    dados = conectado.recv(1024)
    if not dados:
        print("Conexao fechada")
        conectado.close()
        break
    conectado.sendall(dados)
        
        
        
        
        
        
        
        
        
        
        
        
        