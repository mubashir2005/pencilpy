import cv2

image = cv2.imread("trump.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("President Trump", gray_image)

inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, ksize=(21, 21),sigmaX=0, sigmaY=0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)

cv2.imshow("pencil sketch", pencil_sketch)
cv2.imwrite("trump.png",pencil_sketch)
cv2.waitKey(0)