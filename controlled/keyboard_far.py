__author__ = 'Cyber-01'
import pyHook,pythoncom
IP = "192.168.30.13"
MOUSE_PORT = 4567

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
    print '---'

# return True to pass the event to other handlers
    return True

def main():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
   # hm.KeyDown = OnKeyboardEvent
    hm.KeyAll = OnKeyboardEvent
  #  hm.KeyDown = lambda kdn_press: key_press_down(kdn_press, keyboard_sock, procees_list)
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()