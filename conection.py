from djitellopy import Tello
import socket

''''wlp2s0' e 'wlx002e2dc04580' são os nomes das interfaces de rede 
, para checá-los basta digitar o comando ifconfig no Linux / Ubuntu OS.'''

drone_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone_1.setsockopt(socket.SOL_SOCKET, 25, 'wlp2s0'.encode()) 

drone_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone_2.setsockopt(socket.SOL_SOCKET, 25, 'wlx002e2dc04580'.encode())

drone_1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone_2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

#%%Code to takeoff:
drone_1.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))
drone_2.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

#%%Code to land:
drone_1.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
drone_2.sendto('land'.encode(), 0, ('192.168.10.1', 8889)) 

