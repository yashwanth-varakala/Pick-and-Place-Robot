import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red= np.array([161,155,84])
    upper_red= np.array([179,255,255])  
    mask= cv2.inRange(hsv, lower_red, upper_red)

   #conversion from gray scale to binary using threshold
  #  ret,thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_B
    
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('detetion red color',mask)
    #cv2.imshow('guassian threshold',th3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
