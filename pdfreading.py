import pandas
import PyPDF2


#read in financial statements
pdfFileObj = open("applefinancials.pdf", 'rb')

# create a PDFReader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)

# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())

