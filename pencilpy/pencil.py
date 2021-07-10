import cv2

def sketch(image):

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  inverted_image = 255 - gray_image
  blurred = cv2.GaussianBlur(inverted_image, ksize=(21, 21),sigmaX=0, sigmaY=0)

  inverted_blurred = 255 - blurred
  pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
  cv2.imwrite("sketch.png",pencil_sketch)

