import pdfkit
path_wkthmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
pdfkit.from_url("file:///C:/Users/YY/Desktop/NEXT.html.html", "NEXT.pdf", configuration=config)
