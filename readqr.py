import cv2

d =cv2.QRCodeDetector()
val, point, qrcode = d.detectAndDecode(cv2.imread("qrcode.png"))
print(val)