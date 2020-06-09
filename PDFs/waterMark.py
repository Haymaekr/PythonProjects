import sys
import PyPDF2

mark = sys.argv[1]
pdfs = sys.argv[2]


reader1 = PyPDF2.PdfFileReader(open(mark,'rb'))
reader2 = PyPDF2.PdfFileReader(open(pdfs,'rb'))
writer = PyPDF2.PdfFileWriter()
num = reader2.getNumPages()
print(num)
for i in range(0,num):
	page = reader2.getPage(i)
	page.mergePage(reader1.getPage(0))
	writer.addPage(page)
with open("waterMarked.pdf",'wb') as new_file:
	writer.write(new_file)

		


