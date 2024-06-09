import socket

class Swarm:
    def __init__(self, interfaces):
        self.tellos = []
        for interface in interfaces:
            tello_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tello_socket.setsockopt(socket.SOL_SOCKET, 25, interface.encode())
            self.tellos.append(tello_socket)
    
    def send_command(self, command):
        for tello in self.tellos:
            tello.sendto(command.encode(), 0, ('192.168.10.1', 8889))
    
    def takeoff(self):
        self.send_command('takeoff')

    def land(self):
        self.send_command('land')