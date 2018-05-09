__author__ = 'Cyber-01'

from Tkinter import *
from graphics import *
import time
import socket
import Controller

CONNECTION_PORT = 5555
BACKGROUND_PATH = "C:\Vardython\Back.gif"
CONNECTION_TEXT = "Start Connection"
CONTROL_TEXT = "Start Controlling"
IP_ERROR = "The IP that was given is invalid, Try Again"
CONQUERED_ERROR = "The IP That Was Given Is Not Available For Conquering, Try Again"
PASSWORD_ERROR = "No Password Has Been Given, Try Again"

def Image_Background(length, width, win):
    length = length / 2
    width = width / 2
    b = Image(Point(length, width), BACKGROUND_PATH)
    Image.draw(b, win)


def Connection(ip,password,win):
    client_socket = socket.socket() # connecting between the controller and controlled
    client_socket.settimeout(4)
    try:
        client_socket.connect((ip,CONNECTION_PORT))  #
    except:
        error_text = Text(Point(550,650),CONQUERED_ERROR)
        error_text.setTextColor("White")
        error_text.draw(win)
        time.sleep(3)
        error_text.undraw()
        return False
    return client_socket

def Input_Creator(win):
    key_entered = ""
    ip_text = Text(Point(315,400),"Enter IP of The Computer You Want to Control:")
    ip_text.setTextColor("White")
    ip_text.draw(win)

    ip_entry = Entry(Point(550,400),15)
    ip_entry.draw(win)

    continue_text = Text(Point(550,550),"After Filling The Credentials , Press Enter to Continue \r\n If at Anytime You Want to Stop The Connection, Press Pause")
    continue_text.setTextColor("White")
    continue_text.draw(win)

    password_text = Text(Point(365,450),"Enter Password for Connection:")
    password_text.setTextColor("White")
    password_text.draw(win)

    password_entry = Entry(Point(550,450),15)
    password_entry.draw(win)

    while key_entered != "Return":
        key_entered = win.getKey()

    ip = ip_entry.getText()
    password = password_entry.getText()
    try:
        socket.inet_aton(ip)
    except socket.error:
        error_text = Text(Point(550,650),IP_ERROR)
        error_text.setTextColor("White")
        error_text.draw(win)
        time.sleep(3)
        error_text.undraw()
        return False,False

    if password == "":
        error_text = Text(Point(550,650),PASSWORD_ERROR)
        error_text.setTextColor("White")
        error_text.draw(win)
        time.sleep(3)
        error_text.undraw()
        return False,False

    return ip,password

def main():
    win = GraphWin("Control & Conquer", 1100, 800)
    Image_Background(1100, 800, win)

    title = Text(Point(550,200),"Control & Conquer")
    title.setSize(54)
    title.setFace("black ops one")
    title.draw(win)


    ip,password = Input_Creator(win)
    while ip is False:
       ip,password = Input_Creator(win)


    client_socket = Connection(ip,password,win)
    while client_socket is False:
        ip,password = False,False
        while ip is False:
            ip,password = Input_Creator(win)
        client_socket = Connection(ip,password,win)

    client_socket.send(CONNECTION_TEXT)
    client_socket.settimeout(None)
    password_check = client_socket.recv(1024)  # The password that the conquested sends
    if password_check == password:
        client_socket.send(CONTROL_TEXT)
        client_socket.close()
        Controller.main()



    win.close()


if __name__ == '__main__':
    main()