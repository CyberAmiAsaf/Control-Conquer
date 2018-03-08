__author__ = 'Cyber-01'
import win32api,win32con
import socket
KEYBOARD_PORT = 5678

def key_press(data):
    key = data[0][1:]
    key = int(key,16)
    win32api.keybd_event(key,0,0,0)


def key_release(data):
    key = data[0][1:]
    key = int(key,16)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)

def main():
    keyboard_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Client Startup to udp
    keyboard_socket.bind(('0.0.0.0',KEYBOARD_PORT))
    while True:
        try:
            data = keyboard_socket.recvfrom(1024)
            if data[0][0] == "*":
                key_press(data)
            if data[0][0] == "^":
                key_release(data)
        except:
            continue




if __name__ == '__main__':
    main()