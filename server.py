import socket
import numpy as np
import cv2

HOST = ''              # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print(tcp.getsockname())


while True:
    con, cliente = tcp.accept()
    con2, cliente2 = tcp.accept()
    print 'Concetado por', cliente
    print 'Concetado por', cliente2
    
    s=""
    while True:
        #msg = con.recv(1024)
        #if not msg: break
        #print cliente, msg
        
        s=""
        con.send ("1")
        while(len(s) < (16896*60)):
            data = con.recv(16896)
    
            s += data
            con.send ("1")
    
        
        
        if(len(s) == 1013760):
            frame = np.fromstring (s,dtype=np.uint8)
            frame = frame.reshape(480, 704, 3)
            fshow = frame.copy()
    
            cv2.imshow('frame ser',fshow)
            cv2.waitKey(1)
        else:
            print("#################")
    
        s=""
        
        con2.send ("1")
        while(len(s) < (16896*60)):
            data = con2.recv(16896)
    
            s += data
            con2.send ("1")
    
        
        
        if(len(s) == 1013760):
            frame = np.fromstring (s,dtype=np.uint8)
            frame = frame.reshape(480, 704, 3)
            fshow = frame.copy()
    
            cv2.imshow('frame ser2',fshow)
            cv2.waitKey(1)
        else:
            print("#################")
        
        
        
    print 'Finalizando conexao do cliente', cliente
    con.close()