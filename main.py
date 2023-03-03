import PyPDF3
import pyttsx3
import pdfplumber

# File of the pdf you want to convert.
file = 'filename.pdf'

pdf_file = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(pdf_file)

pages = pdfReader.numPages

ExtractedText = ""

with pdfplumber.open(file) as pdf:
    for num in range(0, pages):
        page = pdf.pages[num]
        text = page.extract_text()
        ExtractedText += text

engine = pyttsx3.init()
# Default Speed Rate is 200. Change number below to suit your preference speed.
rate = engine.setProperty('rate', 185)
engine.say(ExtractedText)
engine.runAndWait()