__author__ = 'Vardi'


import cv2
import socket
END_DATA_MESSAGE = "No More Data"
def main():
    print "Client Searching"
    client_socket = socket.socket()
    client_socket.connect(("192.168.30.31",2345))  # Client Startup
    print "Server Found"
    cv2.namedWindow("image",cv2.WND_PROP_FULLSCREEN)  # Put Window to Fullscreen mode
    cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)  # Set Properties of window to fullscreen


    while True:
        try:
            data = client_socket.recv(5000000)  # Receive all of the image's data
            img_file = open("fullscreen.png",'wb')
            img_file.write(data)  # Write data to new image file
            img_file.close()
            img = cv2.imread("fullscreen.png")  # Open image with cv2
            cv2.imshow("image" ,img)  # Show the image onscreen
            cv2.waitKey(1)  # Wait for Key 1 second, if not continue
        except:
            continue



if __name__ == '__main__':
	main()