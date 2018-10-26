import socket
import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://192.168.1.109:554/user=admin&password=raspcam&channel=1&stream=0.sdp?")


HOST = '192.168.1.10'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
tcp.send("1")
print 'Para sair use CTRL+X\n'

#msg = raw_input()


ret, frame = cap.read()
    
d = frame.flatten ()
s = d.tostring ()

e = 1

while((len(s) / e) > 63000):
    e += 1

taxa = len(s) / e


data = tcp.recv(1)
tcp.send(str('%05d' % taxa))
data = tcp.recv(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame cli',frame)
    cv2.waitKey(1)
    
    d = frame.flatten ()
    s = d.tostring ()
    
    topo = 0
    i = 0
    
    #tcp.send (str('%010d' % len(s)))
    while(i * taxa < len(s)):
        
        
        tcp.send (s[i*taxa:(i+1)*taxa])
        data = tcp.recv(1)
        
        i = i + 1
    
    print(len(s))
    #tcp.send (msg)
    #msg = raw_input()
tcp.close()