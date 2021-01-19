import cv2
import numpy as np
import glob
import os
logo = cv2.imread(".\mantej.png")
logo=cv2.resize(logo,(80,80))
h_logo, w_logo, _ = logo.shape

#cv2.imshow('logo',logo)
#cv2.waitKey(0)

#cap = cv2.VideoCapture('E:\mantej\python\OFFICE_emilence\computer_vision\Artificial-Eyeliner\Media\Sample Video.mp4')
cap = cv2.VideoCapture(0)
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
#cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    ret, frame = cap.read()
    img=cv2.resize(frame,(680,480))
    h_img, w_img, _ = img.shape
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)
    top_y = center_y - int(h_logo / 2)
    left_x = int(1.5*(center_x)) + int(w_logo)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo
     # Get ROI
    roi = img[top_y: bottom_y, left_x: right_x]
    #cv2.imshow('roi',roi)
    #Add the Logo to the Roi
    #print(roi.shape,logo.shape)
    result = cv2.addWeighted(roi, 1, logo, 1, 0)
    # Replace the ROI on the image
    img[top_y: bottom_y, left_x: right_x] = result
    #out.write(img)
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()