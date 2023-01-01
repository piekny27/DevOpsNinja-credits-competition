from flask import render_template
from flask import make_response
import pdfkit

pdfOptions = {
    "orientation": "portrait",
    "page-size": "A4",
    "margin-top": "2.0cm",
    "margin-right": "2.0cm",
    "margin-bottom": "2.0cm",
    "margin-left": "2.0cm",
    "encoding": "UTF-8",
}

class PDFGenerator:
    def __init__(self, data): 
        self.data = data

    def getPDF(self):
        html = render_template("summaryPDF.html", data=self.data)
        pdf = pdfkit.from_string(html, options=pdfOptions)
        return pdf

    def getResponse(self):
        pdf = self.getPDF()
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=podsumowanie.pdf"
        return response
