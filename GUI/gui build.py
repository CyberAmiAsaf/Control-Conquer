__author__ = 'Cyber-01'

from Tkinter import *
from graphics import *
import time
IMAGE_PATH = "C:\Vardython\Back.gif"

def Image_Background(length,width,win):

    length = length / 2
    width = width / 2

    b = Image(Point(length,width),IMAGE_PATH)
    Image.draw(b,win)



def main():
    win = GraphWin("Command & Conquer",1100,800)
    Image_Background(1100,800,win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()