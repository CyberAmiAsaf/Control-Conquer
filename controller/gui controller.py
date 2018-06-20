from Tkinter import *
from graphics import *
import time
import socket
import Controller

CONNECTION_PORT = 5555
BACKGROUND_PATH = "C:\Vardython\Background.gif"
CONNECTION_TEXT = "Start Connection"
CONTROL_TEXT = "Start Controlling"
IP_ERROR = "The IP that was given is invalid, Try Again"
CONQUERED_ERROR = "The IP That Was Given Is Not Available For Conquering, Try Again"
PASSWORD_ERROR = "No Password Has Been Given, Try Again"
WINDOW_WIDTH = 1100
WINDOW_LENGTH = 800

def Image_Background(length, width, win):
    """
    A function that changes the background of the window
    """
    length = length / 2
    width = width / 2
    b = Image(Point(length, width), BACKGROUND_PATH)
    Image.draw(b, win)


def Connection(ip,password,win):
    """
    A function that connects between the controller and the conquested
    """
    client_socket = socket.socket()
    client_socket.settimeout(4)
    try:
        client_socket.connect((ip,CONNECTION_PORT))  # checking if the server is ready to be conquested
    except:
        error_text = Text(Point(550,650),CONQUERED_ERROR)
        error_text.setTextColor("White")
        error_text.draw(win)
        time.sleep(3)
        error_text.undraw()
        return False
    return client_socket

def Input_Creator(win):
    """
    A function that builds the input boxes and checks them is they are valid
    """
    key_entered = ""
    ip_text = Text(Point(315,400),"Enter IP of The Computer You Want to Control:")  # IP input box
    ip_text.setTextColor("White")
    ip_text.draw(win)

    ip_entry = Entry(Point(550,400),15)
    ip_entry.draw(win)

    exit_text = Text(Point(550,550),"After Filling The Credentials , Press Enter to Continue \r\n If at Anytime You Want to Stop The Connection, Press Pause")
    exit_text.setTextColor("White")
    exit_text.draw(win)

    pause_text = Text(Point(550,605),"If at Anytime During the Communication, You Would Want to Switch Between the Conquested's Screen and Your Own and Back, Press End")
    pause_text.setTextColor("White")
    pause_text.draw(win)

    password_text = Text(Point(365,450),"Enter Password for Connection:") # password input box
    password_text.setTextColor("White")
    password_text.draw(win)

    password_entry = Entry(Point(550,450),15)
    password_entry.draw(win)

    while key_entered != "Return":
        key_entered = win.getKey()

    ip = ip_entry.getText()
    password = password_entry.getText()
    try:
        socket.inet_aton(ip)  # checks if the IP address is real
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
    win = GraphWin("Control & Conquer", WINDOW_WIDTH, WINDOW_LENGTH)
    Image_Background(WINDOW_WIDTH, WINDOW_LENGTH, win)

    title = Text(Point(550,200),"Control & Conquer")
    title.setSize(54)
    title.setFace("black ops one")
    title.draw(win)


    ip,password = Input_Creator(win)
    while ip is False:
       ip,password = Input_Creator(win)


    client_socket = Connection(ip,password,win)
    while client_socket is False:  # while the conquested is not connected
        ip,password = False,False
        while ip is False:  # while the IP address is not valid
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