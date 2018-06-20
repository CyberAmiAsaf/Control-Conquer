__author__ = 'Cyber-01'


from Tkinter import *
from graphics import *
import socket
import Conquested

CONNECTION_PORT = 5555
BACKGROUND_PATH = "C:\Vardython\Background.gif"
CONNECTION_TEXT = "Start Connection"
CONTROL_TEXT = "Start Controlling"
WINDOW_WIDTH = 1100
WINDOW_LENGTH = 800

def Image_Background(length, width, win):
    """
    The function that changes the background of the window
    """
    length = length / 2
    width = width / 2
    b = Image(Point(length, width), BACKGROUND_PATH)
    Image.draw(b, win)


def main():
    key_entered = ""
    win = GraphWin("Control & Conquer", WINDOW_WIDTH, WINDOW_LENGTH)
    Image_Background(WINDOW_WIDTH, WINDOW_LENGTH, win)

    title = Text(Point(550,200),"Control & Conquer")
    title.setFace('black ops one') # Sets the title's font
    title.setSize(54)
    title.draw(win)

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',CONNECTION_PORT))  # Start the socket's server
    server_socket.listen(5)
    (controller_socket, address) = server_socket.accept()
    connection_text = controller_socket.recv(1024)
    if connection_text == CONNECTION_TEXT:  # If the data that was sent is a connection message for the controller
        password_text = Text(Point(365,450),"Enter Password for Connection:")
        password_text.setTextColor("White")  # The password input box
        password_text.draw(win)

        password_entry = Entry(Point(550,450),15)
        password_entry.draw(win)
        continue_text = Text(Point(550,550),"After Filling The Credentials , Press Enter to Continue")
        continue_text.setTextColor("White")  # The message at the bottom
        continue_text.draw(win)

        while key_entered != "Return":
            key_entered = win.getKey()  # Don't read the text in the password input box until the conquested presses Enter
        password = password_entry.getText()

        controller_socket.send(password)

        control_text = controller_socket.recv(1024)
        print control_text
        if control_text == CONTROL_TEXT:
            win.close()
            server_socket.close()
            Conquested.main()






if __name__ == '__main__':
    main()