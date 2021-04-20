import numpy as np
import cv2

canvas = np.ones([500, 500, 3], 'uint8')*255
color = (0, 0, 0)
line_width = -1
radius = 1
point = (0, 0, 0)
pressed = False


def click(event, x, y, flag, param):
    global canvas, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x, y), radius, color, line_width)
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, (x, y), radius, color, line_width)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False


cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", click)

while True:
    cv2.imshow("Canvas", canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255, 0, 0)
    elif ch & 0xFF == ord('g'):
        color = (0, 255, 0)

cv2.destroyAllWindows()
