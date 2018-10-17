import socket
import numpy as np
import cv2




HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
tcp.send("2")
print 'Para sair use CTRL+X\n'

#msg = raw_input()


taxa = tcp.recv(5)
print("taxa"+taxa)
tcp.send("1")
taxa = int(taxa)

while True:
    
    s=""
    
    while(len(s) < (33792*30)):
        
        data = tcp.recv(taxa)
    
        s += data
        tcp.send ("1")
    
        
        
    print("--------------------------")
    
    if(len(s) == 1013760):
        frame = np.fromstring (s,dtype=np.uint8)
        frame = frame.reshape(480, 704, 3)
        fshow = frame.copy()
    
        cv2.imshow('frame cli2',fshow)
        cv2.waitKey(1)
    else:
        print("##########################")
    
    
    

    
    
    #tcp.send (msg)
    #msg = raw_input()
tcp.close()