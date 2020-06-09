import sys
import PyPDF2

input = sys.argv[1:]

def pdfMerger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write('combined.pdf')
		

pdfMerger(input)