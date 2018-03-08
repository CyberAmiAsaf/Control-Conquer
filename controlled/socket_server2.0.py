__author__ = 'Vardi'
import socket
import time
from PIL import ImageGrab
SCREEN_PORT = 2346
DELAY_TIME = 0.05
SCREENSHOT_NAME = "scrn.png"
def main():
    print "Server Running"
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',SCREEN_PORT))  # Start the socket's server
    server_socket.listen(5)
    (new_socket, address) = server_socket.accept()
    print "Client Connected"
    last_binary_data = ""
    while True:
        last_binary_data = ""
        img = ImageGrab.grab(bbox=None)  # Take screenshot
        img.save(SCREENSHOT_NAME)  # Save screenshot
        fp = open(SCREENSHOT_NAME,'rb')  # open screenshot file to read
        data = fp.read()  # Read all
        while data != last_binary_data:  # while not all the data is sent
            new_socket.send(data)  # Send all data
            last_binary_data = data
        fp.close() # Close file
        time.sleep(DELAY_TIME)  # Delay in order to boost quality


if __name__ == '__main__':
	main()