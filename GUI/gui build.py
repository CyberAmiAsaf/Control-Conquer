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

def Image_Background(length, width, win):
    length = length / 2
    width = width / 2
    b = Image(Point(length, width), BACKGROUND_PATH)
    Image.draw(b, win)



def main():
    win = GraphWin("Command & Conquer", 1100, 800)
    Image_Background(1100, 800, win)

    title = Text(Point(500,200),"Command & Conquer")
    title.setSize(36)
    title.draw(win)



    ip_text = Text(Point(380,400),"Enter IP of Your Computer:")
    ip_text.setTextColor("White")
    ip_text.draw(win)

    ip_entry = Entry(Point(550,400),15)
    ip_entry.draw(win)

    continue_text = Text(Point(550,550),"After Filling The Credentials , Press Anywhere to Continue")
    continue_text.setTextColor("White")
    continue_text.draw(win)

    password_text = Text(Point(365,450),"Enter Password for Connection:")
    password_text.setTextColor("White")
    password_text.draw(win)

    password_entry = Entry(Point(550,450),15)
    password_entry.draw(win)
    win.getMouse()




    ip = ip_entry.getText()
    password = password_entry.getText()


    #win.getMouse()
   # testText = Text(Point(500,300), ip)
    #testText.draw(win)

    #exitText = Text(Point(200,50), 'Click anywhere to quit')
    #exitText.draw(win)
    #win.getMouse()

    #win.getMouse()
    client_socket = socket.socket() # connecting between the controller and controlled
    client_socket.connect((ip,CONNECTION_PORT))  #
    client_socket.send(CONNECTION_TEXT)
    password_check = client_socket.recv(1024)  # The password that the conquested sends
    if password_check == password:
        client_socket.send(CONTROL_TEXT)
        client_socket.close()
        Controller.main()



    win.close()


if __name__ == '__main__':
    main()