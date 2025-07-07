import cv2
import os
cascade_path = "haarcascade_frontalface_default.xml"
if not os.path.exists(cascade_path):
    print("❌ XML file missing!")
    exit()

face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread("test2.jpg")
if img is None:
    print("❌ Image not found or failed to load.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Detected Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
