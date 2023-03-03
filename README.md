# PDF_to_audio_converter

This Python script utilizes three libraries, PyPDF3, pdfplumber, and pyttsx3, to convert a PDF file into an audible format.

To use this script, replace "filename.pdf" with the name of the PDF file that you want to convert. Make sure that the PDF file is in the same directory as the script.

The script works by first opening the PDF file and extracting the number of pages. It then uses pdfplumber to extract the text from each page and concatenates it into a single string. Finally, it uses pyttsx3 to convert the extracted text into audio and plays it back to the user.

By default, the script sets the speech rate to 185, but you can adjust this value to suit your preference.

Note: Before running the script, make sure that you have installed the required libraries (PyPDF3, pdfplumber, and pyttsx3) on your system. You can install these libraries using pip, the Python package installer. For example, you can run "pip install PyPDF3" to install PyPDF3.
