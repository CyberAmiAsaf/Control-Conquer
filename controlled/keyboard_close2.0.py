__author__ = 'Cyber-01'
import pyHook,pythoncom
import win32api,win32con
import socket
KEYBOARD_PORT = 5678

VK_CODE = {'Back': 0x08, 'Tab': 0x09, 'Clear/*': 0x0C, 'Return': 0x0D, 'shift': 0x10, 'ctrl': 0x11, 'alt': 0x12,
           'Pause': 0x13,
           'Capital': 0x14, 'Escape': 0x1B, 'Space': 0x20, 'Prior': 0x21, 'Next': 0x22, 'End': 0x23, 'Home': 0x24,
           'Left': 0x25,
           'Up': 0x26, 'Right': 0x27, 'Down': 0x28, 'select': 0x29, 'print': 0x2A, 'execute': 0x2B, 'Snapshot': 0x2C,
           'Insert': 0x2D,
           'Delete': 0x2E, 'help': 0x2F, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36,
           '7': 0x37, '8': 0x38,
           '9': 0x39, 'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49,
           'J': 0x4A, 'K': 0x4B,
           'L': 0x4C, 'M': 0x4D, 'N': 0x4E, 'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55,
           'V': 0x56, 'W': 0x57,
           'X': 0x58, 'Y': 0x59, 'Z': 0x5A, 'Numpad0': 0x60, 'Numpad1': 0x61, 'Numpad2': 0x62, 'Numpad3': 0x63,
           'Numpad4': 0x64,
           'Numpad5': 0x65, 'Numpad6': 0x66, 'Numpad7': 0x67, 'Numpad8': 0x68, 'Numpad9': 0x69, 'Multiply': 0x6A,
           'Add': 0x6B,
           'separator_key': 0x6C, 'Subtract': 0x6D, 'Decimal': 0x6E, 'Divide': 0x6F, 'F1': 0x70, 'F2': 0x71, 'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74, 'F6': 0x75, 'F7': 0x76, 'F8': 0x77, 'F9': 0x78, 'F10': 0x79, 'F11': 0x7A, 'F12': 0x7B,
           'F13': 0x7C, 'F14': 0x7D,
           'F15': 0x7E, 'F16': 0x7F, 'F17': 0x80, 'F18': 0x81, 'F19': 0x82, 'F20': 0x83, 'F21': 0x84, 'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87, 'Numlock': 0x90, 'Scroll': 0x91, 'Lshift': 0xA0, 'Rshift ': 0xA1, 'Lcontrol': 0xA2,
           'Rcontrol': 0xA3,
           'Lmenu': 0xA4, 'Rmenu': 0xA5, 'browser_back': 0xA6, 'browser_forward': 0xA7, 'browser_refresh': 0xA8,
           'browser_stop': 0xA9, 'browser_search': 0xAA, 'browser_favorites': 0xAB, 'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD, 'volume_Down': 0xAE, 'volume_up': 0xAF, 'next_track': 0xB0, 'previous_track': 0xB1,
           'stop_media': 0xB2, 'play/pause_media': 0xB3, 'start_mail': 0xB4, 'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7, 'attn_key': 0xF6, 'crsel_key': 0xF7, 'exsel_key': 0xF8, 'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE, 'Oem_Plus': 0xBB, 'Oem_Comma': 0xBC, 'Oem_Minus': 0xBD, 'Oem_Period': 0xBE, 'Oem_2': 0xBF,
           'Oem_3': 0xC0, 'Oem_1': 0xBA, 'Oem_4': 0xDB, 'Oem_5': 0xDC, 'Oem_6': 0xDD, "Oem_7": 0xDE}



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
            print data
            if data[0][0] == "*":
                key_press(data)
            if data[0][0] == "^":
                key_release(data)




        except:
            continue














if __name__ == '__main__':
    main()