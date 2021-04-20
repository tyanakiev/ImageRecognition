import numpy as np
import cv2


bw = cv2.imread("static/test_images/liverpool.jpg", 0)
cv2.imshow("BW image", bw)

ret, thresh_basic = cv2.threshold(bw, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh Basic", thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Thresh Adaptive", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()