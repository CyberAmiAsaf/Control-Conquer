__author__ = 'Cyber-01'


import socket
import time
from PIL import ImageGrab
import multiprocessing
import win32api,win32con
import sys

SCREEN_PORT = 2346
MOUSE_PORT = 3456
KEYBOARD_PORT = 5678
SCREEN_DELAY_TIME = 0.05
SCREENSHOT_NAME = "scrn.png"



def screen():
    """
    A function that takes screenshots throughout the connection and sends them to the controller
    """
    print "Server Running"
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',SCREEN_PORT))  # Start the socket's server
    server_socket.listen(5)
    (new_socket, address) = server_socket.accept()
    print "Client Connected"
    last_binary_data = ""
    while True:
        last_binary_data = ""
        img = ImageGrab.grab(bbox=None)  # Take screen shot
        img.save(SCREENSHOT_NAME)  # Save screen shot
        fp = open(SCREENSHOT_NAME,'rb')  # open screen shot file to read
        data = fp.read()  # Read all
        while data != last_binary_data:  # while not all the data is sent
            new_socket.send(data)  # Send all data
            last_binary_data = data
        fp.close() # Close file
        time.sleep(SCREEN_DELAY_TIME)  # Delay in order to boost quality


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


def mouse():
    """
    A function that receives the mouse movement from the controller and acts accordingly
    """
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
                        mouse_click(data[1],x,y)  # Left mouse Click
                    else:
                        mouse_release(data[1],x,y) # Left mouse Release

                if data[1] == "R":
                    if data[0] == "*":
                        mouse_click(data[1],x,y) # Right mouse Click
                    else:
                        mouse_release(data[1],x,y) # Right mouse Release

                if data[1] == "M":
                    if data[0] == "*":
                        mouse_click(data[1],x,y) # Middle mouse Click
                    else:
                        mouse_release(data[1],x,y) # Middle mouse Release

                if data[1] == "1":
                    mouse_wheel_movement(data, x, y)  # Mouse wheel movement
            if len(data) == 1:
                mouse_wheel_movement(data, x, y) # Mouse wheel movement

        except:
            pass


def key_press(data):
    """
    A function that receives the key that the controller sent and presses them
    """
    key = data[0][1:]
    key = int(key,16)  # Convert hex string to int
    win32api.keybd_event(key,0,0,0)


def key_release(data):
    """
    A function that receives the key that the controller sent and releases them
    """
    key = data[0][1:]
    key = int(key,16) # Convert hex string to int
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)

def keyboard(process_list):
    """
    A function that receives the controller's keyboard events and acts accordingly
    """
    keyboard_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Client Startup to udp
    keyboard_socket.bind(('0.0.0.0',KEYBOARD_PORT))
    while True:
        try:
            data = keyboard_socket.recvfrom(1024)
            if data[0] == "Pause":
                process_list[0].terminate()
                process_list[1].terminate()
                sys.exit()
            elif data[0][0] == "*":
                key_press(data)
            if data[0][0] == "^":
                key_release(data)
        except:
            continue



def main():

    process_list = []

    screen_process = multiprocessing.Process(target= screen)
    screen_process.start()
    process_list.append(screen_process)

    mouse_process = multiprocessing.Process(target=mouse)
    mouse_process.start()
    process_list.append(mouse_process)

    keyboard_process = multiprocessing.Process(target=keyboard(process_list))
    keyboard_process.start()
    process_list.append(keyboard_process)

if __name__ == '__main__':
    main()