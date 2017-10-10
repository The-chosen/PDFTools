from PyPDF2 import PdfFileMerger

pdfs = ['NEXT.pdf', 'BlockChain.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('1.pdf', 'wb') as fout:
    merger.write(fout)
