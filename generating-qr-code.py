import pyqrcode
import cv2
import png

link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc"

qrcode = pyqrcode.create(link)

qrcode.png("Youtube.png", scale=5)

img=cv2.imread('Youtube.png')
img_grayscale = cv2.imread('Youtube.png', 0)

cv2.imshow('graycsale image', img_grayscale)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('Youtube.png', img_grayscale)
print("------------------------------------------------------------------")
