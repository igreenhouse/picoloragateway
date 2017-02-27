from network import LoRa
import struct
import socket
lora=LoRa(mode=LoRa.LORA,frequency=868000000, sf=7)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW) #create a LoRa socket
i=0
while 1:
    t=s.recv(4)
    rx_data= struct.unpack('f', t)
    print(rx_data)
    if i==1:
        temperature = rx_data
    elif i==2:
        humidite = rx_data
    elif i==3:
        numero=rx_data
        print("Releve, temperature : ")
        print(temperature)
        print(", humidite : ")
        print(humidite)
        print("numero : ")
        print(numero)
    i = (i+1)%4
