from competition import app
from competition.forms import AgroCreditForm, InvestCreditForm
from competition.dbModels import DBConnection, ClientData, CreditData, InvestCreditData, AgroCreditData
from competition.schemas import AgroCreditDataSchema, InvestCreditDataSchema
from flask import render_template

db = DBConnection()
db._engine.create_all()

@app.route("/")
@app.route("/credits")
def credits_page():
    return render_template("credits.html")

@app.route("/credits/agro", methods=['GET', 'POST'])
def agro_page():
    form = AgroCreditForm()
    if form.validate_on_submit():
        newClientData = ClientData(fullname = form.fullname.data)
        db.session.add(newClientData)
        db.session.commit()
        newCreditData = CreditData(loanAmount = form.loanAmount.data,
                        interestRate = form.interestRate.data)
        db.session.add(newCreditData)
        db.session.commit()
        newAgroCreditData = AgroCreditData(clientData_id=newClientData.id,
                        conclusionDate=form.conclusionDate.data,
                        conclusionPeriod=form.conclusionPeriod.data,
                        creditData_id= newCreditData.id,
                        repaymentScheduleType = form.repaymentScheduleType.data)
        db.session.add(newAgroCreditData)
        db.session.commit()
        agroCredit_schema = AgroCreditDataSchema()
        creditData = agroCredit_schema.dump(newAgroCreditData)
        creditData['creditType'] = "agro"
        return render_template("credits-agro.html", form=form, data=creditData)
    return render_template("credits-agro.html", form=form)

@app.route("/credits/invest", methods=['GET', 'POST'])
def invest_page():
    form = InvestCreditForm()
    if form.validate_on_submit():
        newClientData = ClientData(fullname = form.fullname.data)
        db.session.add(newClientData)
        db.session.commit()
        newCreditData = CreditData(loanAmount = form.loanAmount.data,
                        interestRate = form.interestRate.data)
        db.session.add(newCreditData)
        db.session.commit()
        newInvestCreditData = InvestCreditData(clientData_id=newClientData.id,
                        conclusionDate=form.conclusionDate.data,
                        conclusionPeriod=form.conclusionPeriod.data,
                        investmentValue=form.investmentValue.data,
                        ownContribution=form.ownContribution.data,
                        commission=form.commission.data,
                        creditData_id= newCreditData.id,
                        repaymentScheduleType = form.repaymentScheduleType.data)
        db.session.add(newInvestCreditData)
        db.session.commit()
        investCredit_schema = InvestCreditDataSchema()
        creditData = investCredit_schema.dump(newInvestCreditData)
        creditData['creditType'] = "invest"
        return render_template("credits-invest.html", form=form, data=creditData)
    return render_template("credits-invest.html", form=form)

@app.route("/api/gen-pdf/<string:type>-<int:id>", methods=['GET', 'POST'])
def genPDF_page(type, id):
    pass