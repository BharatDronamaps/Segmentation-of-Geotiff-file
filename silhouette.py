import cv2
import numpy

frame = cv2.imread('crop_img.png')

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

hsv_channels = cv2.split(hsv)

rows = frame.shape[0]
cols = frame.shape[1]

for i in range(0, rows):
    for j in range(0, cols):
        h = hsv_channels[0][i][j]

        if h > 25 and h < 150:
            hsv_channels[2][i][j] = 255
        else:
            hsv_channels[2][i][j] = 0

#cv2.imshow("show", hsv_channels[0])
#cv2.imshow("show2", hsv_channels[2])

#cv2.waitKey(0)
cv2.imwrite('output.tif', hsv_channels[2])
