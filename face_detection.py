import cv2  # Import the OpenCV library

# Load the pre-trained face detection model (Haar Cascade) from the specified XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image file where face detection will be performed
img = cv2.imread('test.jpeg')

# Convert the image to grayscale as face detection generally performs better on grayscale images
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Detect faces in the grayscale image
# detectMultiScale detects objects of different sizes, and returns a list of rectangles, each representing a detected face
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over the list of detected faces and draw rectangles around them
for (x, y, w, h) in faces:
    # Draw a rectangle around each face in the original image
    # The rectangle is drawn from the top-left corner (x, y) to the bottom-right corner (x + w, y + h)
    # The rectangle color is set to blue (225, 0, 0) and the thickness of the rectangle border is 2 pixels
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# Display the image with the detected faces in a window titled 'img'
cv2.imshow('img', img)

# Wait indefinitely for any key press before closing the display window
cv2.waitKey()

# Save the image with the detected faces to a new file called "face_detected.jpg"
cv2.imwrite("face_detected.jpg", img)
