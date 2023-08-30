import cv2
import numpy as np


sharp= np.array([[
    0,-1,0,
    -1,5,-1,
    0,-1,0
]])
source = cv2.VideoCapture(0)

win_name ='filter demo'

cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)

PREVIEW = 0

CANNY= 1
image_filter= PREVIEW

result=None
while True:
    has_frame ,frame = source.read()
    if not has_frame:
        break
    frame = cv2.flip(frame,1)
    if image_filter == CANNY:
        result =cv2.Canny(frame,50,150)
    else:
        # cv2.filter2D(frame, -1, sharp)
        # cv2.GaussianBlur(frame, (25, 25), 0, 0)
        result = frame
    cv2.imshow(win_name,result)

    key = cv2.waitKey(1)
    if key== ord('Q') or key == ord('q') or key==27:
        break
    elif key== ord('C') or key == ord('c'):
        image_filter=CANNY

    elif key== ord('P') or key == ord('p'):
        image_filter=PREVIEW
