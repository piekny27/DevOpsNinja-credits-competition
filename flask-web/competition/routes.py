from competition import app
from competition.dbModels import DBConnection, InvestCreditData, AgroCreditData
from competition.schemas import AgroCreditDataSchema, InvestCreditDataSchema
from competition.calculator import ScheduleCalculator
from competition.pdfGenerator import PDFGenerator

db = DBConnection()

@app.route("/api/gen-pdf/<string:type>-<int:id>", methods=['GET', 'POST'])
def genPDF_page(type, id):
    match type:
        case 'invest':
            investCreditData = InvestCreditData.query.get(id)
            investCredit_schema = InvestCreditDataSchema()
            creditData = investCredit_schema.dump(investCreditData)
            scheduleCalculator = ScheduleCalculator(investCreditData)
            creditData['schedule'] = scheduleCalculator.calculate()
            creditData['creditType'] = "invest"
        case 'agro':
            agroCreditData = AgroCreditData.query.get(id)
            agroCredit_schema = AgroCreditDataSchema()
            creditData = agroCredit_schema.dump(agroCreditData)
            scheduleCalculator = ScheduleCalculator(agroCreditData)
            creditData['schedule'] = scheduleCalculator.calculate()
            creditData['creditType'] = "agro"
    pdf = PDFGenerator(creditData)
    return pdf.getResponse()