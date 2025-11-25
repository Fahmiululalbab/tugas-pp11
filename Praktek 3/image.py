import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Load image
img = cv2.imread('images/contoh.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show result
cv2.imshow("Deteksi Wajah pada Gambar", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
