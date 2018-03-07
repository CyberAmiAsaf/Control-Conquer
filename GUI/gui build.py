__author__ = 'Cyber-01'

from Tkinter import *
from graphics import *
import time

IMAGE_PATH = "C:\Vardython\Back.gif"
HOMEPAGE_TEXT = "Hello Controller \r\n In Order to Start Your Controlling  "

def Image_Background(length, width, win):
    length = length / 2
    width = width / 2
    b = Image(Point(length, width), IMAGE_PATH)
    Image.draw(b, win)


def main():
    win = GraphWin("Command & Conquer", 1100, 800)
    Image_Background(1100, 800, win)

    textEntry = Entry(Point(500,200),10)
    textEntry.draw(win)
    win.getMouse()

    text = textEntry.getText()

    testText = Text(Point(500,300), text)
    testText.draw(win)

    exitText = Text(Point(200,50), 'Click anywhere to quit')
    exitText.draw(win)
    win.getMouse()


    win.close()


if __name__ == '__main__':
    main()