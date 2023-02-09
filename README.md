# Color to B&W Image Conversion App
This is a simple web-based application for converting a color image to a black and white image. The app is built using the Streamlit library and OpenCV library.

## Requirements
The following packages need to be installed to run this code:

- streamlit
- numpy
- PIL (Python Imaging Library)
- opencv-python

## Usage
To run the app, simply run the following command in your terminal:
streamlit run <file_name>.py

where <file_name> is the name of the file containing the code.

After running the command, the app will be accessible in your web browser at http://localhost:8501. To use the app, simply upload an image in either PNG, JPG, or JPEG format using the file uploader in the sidebar. The app will then display the original image in the left column and the converted black and white image in the right column. You can download the black and white image by clicking the download button in the sidebar.

## Limitations
Please note that the quality of the resulting black and white image may depend on the quality of the original image. If the original image has low resolution, the converted image may look pixelated.
