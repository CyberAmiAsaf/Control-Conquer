__author__ = 'Cyber-01'

import socket
import win32con
import win32api
IP = "192.168.30.13"
MOUSE_PORT = 3456




def mouse_click(button,x,y):
    """
    A function that receives which button was clicked and the coordinates of the mouse, and clicks accordingly
    """
    if button == "L":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)

    if button == "R":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)

    if button == "M":
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)


def mouse_release(button,x,y):
    """
    A function that receives which button was released and the coordinates of the mouse, and releases accordingly
    """
    if button == "L":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    if button == "R":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

    if button == "M":
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)


def mouse_wheel_movement(button, x, y):
    """
    A function that receives the mouse wheel's movement and the coordinates of the mouse, and moves accordingly
    """
    if button == "-1":
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,x ,y ,-win32con.WHEEL_DELTA,0)

    if button == "1":
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,x ,y ,win32con.WHEEL_DELTA,0)




def main():
    mouse_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Client Startup to udp
    mouse_socket.bind(('0.0.0.0',MOUSE_PORT))
    while True:
        try:

            data,address = mouse_socket.recvfrom(1024)
            if len(data) > 2:
                position = data.split(",")
                x = int(position[0][1:])
                y = int(position[1][:-1])
                win32api.SetCursorPos((x,y))  # A function that receives the mouse coordinates and sets them accordingly

            if len(data) == 2:
                if data[1] == "L":
                    if data[0] == "*":
                        mouse_click(data[1],x,y)
                    else:
                        mouse_release(data[1],x,y)

                if data[1] == "R":
                    if data[0] == "*":
                        mouse_click(data[1],x,y)
                    else:
                        mouse_release(data[1],x,y)

                if data[1] == "M":
                    if data[0] == "*":
                        mouse_click(data[1],x,y)
                    else:
                        mouse_release(data[1],x,y)

                if data[1] == "1":
                    mouse_wheel_movement(data, x, y)
            if len(data) == 1:
                mouse_wheel_movement(data, x, y)

        except:
            pass




if __name__ == '__main__':
    main()