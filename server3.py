import socket
import numpy as np
import cv2
from asn1crypto._ffi import null

HOST = '192.168.1.104'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print(tcp.getsockname())


while True:
    con = null
    con2 = null
    
    while((con == null) | (con2 == null)):
        cone, clie = tcp.accept()
        tipo = cone.recv(1)
        if(int(tipo) == 1):
            con = cone
            cliente = clie
            print '1 - Conectado por', cliente
        if(int(tipo) == 2):
            con2 = cone
            cliente2 = clie
            print '2 - Conectado por', cliente2
            
    
    
    
    
    
    
    while True:
        #msg = con.recv(1024)
        #if not msg: break
        #print cliente, msg
        
        
        
        
        
        data = con.recv(1)
    
        print(data)
        
        
        con2.send(data)
        
        
        
    print 'Finalizando conexao do cliente', cliente
    con.close()