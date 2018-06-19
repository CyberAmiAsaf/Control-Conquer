__author__ = 'Cyber-01'

import pythoncom, pyHook
import socket
import cv2
import multiprocessing
import sys
import ctypes
import os

IP = "192.168.30.19"
SCREEN_PORT = 2346
MOUSE_PORT = 3456
KEYBOARD_PORT = 5678

def screen(BOOLEAN):
    """
    A function that receives screenshots from the conquested and shows them on the screen
    """
    print "Client Searching"
    client_socket = socket.socket()
    client_socket.connect((IP,SCREEN_PORT))  # Client Startup
    print "Server Found"
    cv2.namedWindow("image",cv2.WND_PROP_FULLSCREEN)  # Put Window to Fullscreen mode
    cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)  # Set Properties of window to fullscreen


    while True:
        try:
            data = client_socket.recv(5000000)  # Receive all of the image's data
            img_file = open("fullscreen.png",'wb')
            img_file.write(data)  # Write data to new image file
            img_file.close()
            if BOOLEAN.value == False:
                cv2.namedWindow("image",cv2.WND_PROP_FULLSCREEN)  # Put Window to Fullscreen mode
                cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)  # Set Properties of window to fullscreen
                img = cv2.imread("fullscreen.png")  # Open image with cv2
                cv2.imshow("image" ,img)  # Show the image onscreen
            else:
                cv2.destroyAllWindows()
                os.remove("fullscreen.png")
            cv2.waitKey(1)  # Wait for Key 1 second, if not continue
        except:
            exit()
            continue



def Right_Click(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a right click event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto('*R',(IP, MOUSE_PORT))
    return True


def Right_Release(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a right click release event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto('^R',(IP, MOUSE_PORT))
    return True



def Left_Click(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a left click event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto('*L',(IP, MOUSE_PORT))
    return True


def Left_Release(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a left click release event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto('^L',(IP, MOUSE_PORT))
    return True


def Mouse_Wheel(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a wheel movement event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto(str(event.Wheel),(IP, MOUSE_PORT))
    return True



def Mouse_Move(event,mouse_socket,BOOLEAN):
    """
    A function that starts when there is a mouse movement event and sends the controlled computer that same event
    """
    if BOOLEAN.value == False:
        mouse_socket.sendto(str(event.Position),(IP, MOUSE_PORT))
    return True


def mouse(BOOLEAN):
    """
    A function that records the mouse movement and sends them to the conquested
    """

    mouse_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Creating a udp client that sends mouse activity

    hm = pyHook.HookManager()     # create a hook manager


    hm.MouseLeftDown = lambda move: Left_Click(move,mouse_socket,BOOLEAN)  # Sets all the mouse's events to their functions
    hm.MouseLeftUp = lambda move: Left_Release(move,mouse_socket,BOOLEAN)
    hm.MouseRightDown = lambda move: Right_Click(move,mouse_socket,BOOLEAN)
    hm.MouseRightUp = lambda move: Right_Release(move,mouse_socket,BOOLEAN)
    hm.MouseWheel = lambda move: Mouse_Wheel(move,mouse_socket,BOOLEAN)
    hm.MouseMove = lambda move: Mouse_Move(move,mouse_socket,BOOLEAN)


    hm.HookMouse()  # Start reading the mouse's activities

    pythoncom.PumpMessages()  # Forever read



def KeyPress(event,keyboard_socket,mouse_process,screen_process, BOOLEAN):
    """
    A function that acts when a keyboard button is pressed and sends it to the conquested
    """
    key_id = event.KeyID
    #print key_id
    if event.GetKey() == "Pause":
        keyboard_socket.sendto("Pause", (IP, KEYBOARD_PORT))
        screen_process.terminate()
        mouse_process.terminate()
        sys.exit()
    if event.GetKey() == "End":
        BOOLEAN.value = not BOOLEAN.value
        print BOOLEAN.value
        print "bbb"
        #keyboard_socket.sendto("End", (IP, KEYBOARD_PORT))
        return True
    if BOOLEAN.value == False:
        keyboard_socket.sendto("*"+hex(key_id), (IP, KEYBOARD_PORT))
    return True

def KeyRelease(event,keyboard_socket,BOOLEAN):
    """
    A function that acts when a keyboard button is released and sends it to the conquested
    """
    key_id = event.KeyID
    if BOOLEAN.value == False:
        keyboard_socket.sendto("^"+hex(key_id), (IP, KEYBOARD_PORT))
    return True


def keyboard(mouse_process,screen_process, BOOLEAN):
    """
    A function that records the keyboard's events and acts accordingly
    """
    keyboard_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Creating a udp client that sends keyboard activity
    hm = pyHook.HookManager() # create a hook manager

    hm.KeyDown = lambda event: KeyPress(event,keyboard_socket,mouse_process,screen_process, BOOLEAN)
    hm.KeyUp = lambda event: KeyRelease(event,keyboard_socket,BOOLEAN)
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()


def main():
    BOOLEAN = multiprocessing.Value(ctypes.c_bool, False)
    process_list = []

    screen_process = multiprocessing.Process(target= screen, args=(BOOLEAN, ))
    screen_process.start()
    process_list.append(screen_process)

    mouse_process = multiprocessing.Process(target=mouse, args=(BOOLEAN, ))
    mouse_process.start()
    process_list.append(mouse_process)

    keyboard(mouse_process,screen_process,BOOLEAN)
    """
    keyboard_process = multiprocessing.Process(target=keyboard, args=(mouse_process,screen_process,BOOLEAN, ))
    keyboard_process.start()
    process_list.append(keyboard_process)
    """


if __name__ == '__main__':
    main()