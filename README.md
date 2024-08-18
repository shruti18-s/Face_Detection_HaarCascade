# Face Detection with OpenCV

This project demonstrates how to perform face detection in images using OpenCV's pre-trained Haar Cascade classifier. The program reads an image, converts it to grayscale, detects faces, and draws rectangles around the detected faces.

## Features

- **Face Detection:** Uses Haar Cascade classifiers to detect faces in images.
- **Image Processing:** Converts images to grayscale for better detection accuracy.
- **Visualization:** Draws rectangles around detected faces.
- **Image Saving:** Saves the output image with detected faces.

## Requirements

- **Python 3.x**
- **OpenCV**

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/face-detection-opencv.git
    cd face-detection-opencv
    ```

2. **Install the required packages:**
    ```bash
    pip install opencv-python
    ```

3. **Download Haar Cascade XML file:**
   - Download `haarcascade_frontalface_default.xml` from [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage

1. **Place your image in the project directory and rename it to `test.jpeg`** or update the script with your image file name.
   
2. **Run the face detection script:**
    ```bash
    python face_detection.py
    ```

3. The image with detected faces will be displayed and saved as `face_detected.jpg`.

## How It Works

- **Load the Haar Cascade Classifier:** The classifier is loaded from the XML file which contains the pre-trained model.
- **Convert Image to Grayscale:** The image is converted to grayscale as face detection works better on grayscale images.
- **Detect Faces:** The `detectMultiScale` method is used to detect faces in the image.
- **Draw Rectangles:** Rectangles are drawn around each detected face.
- **Display and Save:** The processed image is displayed and saved to the disk.

## License

This project is licensed under the MIT License.


