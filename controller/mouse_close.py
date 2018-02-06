__author__ = 'Cyber-01'

import pythoncom, pyHook
import socket
IP = "192.168.30.31"
MOUSE_PORT = 3456


def Right_Click(event,mouse_socket):
    """
    A function that starts when there is a right click event and sends the controlled computer that same event
    """
    mouse_socket.sendto('*R',(IP, MOUSE_PORT))
    return True


def Right_Release(event,mouse_socket):
    """
    A function that starts when there is a right click release event and sends the controlled computer that same event
    """
    mouse_socket.sendto('^R',(IP, MOUSE_PORT))
    return True



def Left_Click(event,mouse_socket):
    """
    A function that starts when there is a left click event and sends the controlled computer that same event
    """
    mouse_socket.sendto('*L',(IP, MOUSE_PORT))
    return True


def Left_Release(event,mouse_socket):
    """
    A function that starts when there is a left click release event and sends the controlled computer that same event
    """
    mouse_socket.sendto('^L',(IP, MOUSE_PORT))
    return True


def Mouse_Wheel(event,mouse_socket):
    """
    A function that starts when there is a wheel movement event and sends the controlled computer that same event
    """
    mouse_socket.sendto(str(event.Wheel),(IP, MOUSE_PORT))
    return True



def Mouse_Move(event,mouse_socket):
    """
    A function that starts when there is a mouse movement event and sends the controlled computer that same event
    """
    mouse_socket.sendto(str(event.Position),(IP, MOUSE_PORT))
    return True

def main():

    mouse_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Creating a udp client that sends mouse activity

    hm = pyHook.HookManager()     # create a hook manager


    hm.MouseLeftDown = lambda move: Left_Click(move,mouse_socket)  # Sets all the mouse's events to their functions
    hm.MouseLeftUp = lambda move: Left_Release(move,mouse_socket)
    hm.MouseRightDown = lambda move: Right_Click(move,mouse_socket)
    hm.MouseRightUp = lambda move: Right_Release(move,mouse_socket)
    hm.MouseWheel = lambda move: Mouse_Wheel(move,mouse_socket)
    hm.MouseMove = lambda move: Mouse_Move(move,mouse_socket)

    hm.HookMouse()  # Start reading the mouse's activities

    pythoncom.PumpMessages()  # Forever read


if __name__ == '__main__':
    main()