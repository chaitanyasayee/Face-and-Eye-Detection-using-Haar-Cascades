# Face and Eye Detection using Haar Cascades

This project demonstrates how to detect faces and eyes in an image using Haar cascades in OpenCV. Haar cascades are trained classifiers capable of identifying specific objects or features within an image.

## Prerequisites
- Python 3.x
- OpenCV library
- Haar cascade files: `haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`

## Installation
1. Install Python by downloading it from the official Python website (https://www.python.org) and following the installation instructions for your operating system.

2. Install OpenCV library using pip:
   ```
   pip install opencv-python
   ```

## Usage
1. Clone or download the project files from the repository.

2. Replace the image path in the code (`C:/Users/91630/Downloads/gg.jfif`) with the path to your own image.

3. Run the Python script, and the output will display the detected faces and eyes in separate images.

## Code Explanation
1. Import the necessary libraries: `cv2` for image processing, `numpy` for numerical computations, and `matplotlib.pyplot` for visualizations.

2. Read the input image and create copies.

3. Load the Haar cascade classifiers for face and eye detection.

4. Define a function `adjusted_detect_face` to detect faces in the image using the face cascade classifier. This function draws rectangles around the detected faces and returns the modified image.

5. Define a function `detect_eyes` to detect eyes in the image using the eye cascade classifier. This function draws rectangles around the detected eyes and returns the modified image.

6. Apply the `adjusted_detect_face` function to the image copy, and display the detected faces using `plt.imshow()`.

7. Save the image with detected faces using `cv2.imwrite()`.

8. Apply the `detect_eyes` function to another image copy, and display the detected eyes using `plt.imshow()`.

9. Save the image with detected eyes using `cv2.imwrite()`.

10. Create a weighted combination of the images with detected faces and eyes using `cv2.addWeighted()`. This produces an overlay of the two images.

11. Display the final image with the overlay using `plt.imshow()`.

12. Save the final image using `cv2.imwrite()`.

13. Show the image using `cv2.imshow()`, and wait for a key press to close the window.

14. Clean up and close all windows using `cv2.destroyAllWindows()`.

## Result
The script detects faces and eyes in the input image and saves three images: one with detected faces, one with detected eyes, and one with a combination of both. The images are also displayed during the execution of the script.# python-open-cv 
I have used an image of Israeli actress Gal Gadot for face and eye detection. Here is the original image:


![gg](https://user-images.githubusercontent.com/84325486/130352357-1ffe8688-b81f-4f35-b449-cf05d5f1fa8a.jpeg)

The script detects faces and eyes in the image and produces the following results:

1.Detected faces:



![gg](https://user-images.githubusercontent.com/84325486/130352299-8799738f-eaf0-4e71-84db-7615fe94a2e9.png)


