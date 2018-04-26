__author__ = 'Cyber-01'


from Tkinter import *
from graphics import *
import time
import socket
import Conquested

CONTROLLER_IP = "192.168.30.28"
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
    key_entered = ""
    win = GraphWin("Command & Conquer", 1100, 800)
    Image_Background(1100, 800, win)

    title = Text(Point(500,200),"Command & Conquer")
    title.setSize(36)
    title.draw(win)

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',CONNECTION_PORT))  # Start the socket's server
    server_socket.listen(5)
    (controller_socket, address) = server_socket.accept()
    connection_text = controller_socket.recv(1024)
    if connection_text == CONNECTION_TEXT:
        password_text = Text(Point(365,450),"Enter Password for Connection:")
        password_text.setTextColor("White")
        password_text.draw(win)

        password_entry = Entry(Point(550,450),15)
        password_entry.draw(win)
        continue_text = Text(Point(750,550),"After Filling The Credentials , Press Enter to Continue")
        continue_text.setTextColor("White")
        continue_text.draw(win)

        while key_entered != "Return":
            key_entered = win.getKey()
        password = password_entry.getText()

        #win.getMouse()
        controller_socket.send(password)

        control_text = controller_socket.recv(1024)
        print control_text
        if control_text == CONTROL_TEXT:
            server_socket.close()
            Conquested.main()

        win.close()



if __name__ == '__main__':
    main()