# PDF to Audio book by @mlwithrish
import pyttsx3
import PyPDF2
#open required pdf file
book = open('mybook.pdf','rb') #myboook.pdf -> book name
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages
play = pyttsx3.init()
print('Playing Audio Book')

for num in range(0, num_pages): #iterating through all pages
	page = pdf_reader.getPage(num)
	data = page.extractText()  #extracting text

	play.say(data)
	play.runAndWait()