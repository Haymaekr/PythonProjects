import PyPDF2


with open("dummy.pdf", 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	page = reader.getPage(0)
	page = page.rotateClockwise(180)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open("tilted.pdf", 'wb') as new_file:
		writer.write(new_file)
