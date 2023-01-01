from competition import db
from competition.enums import RepaymentScheduleType

def Singleton(class_):
    instances = {}
    def GetInstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return GetInstance 

@Singleton
class DBConnection():
    def __init__(self):
        self._engine = db
        Session = self._engine.session
        self.session = Session

class ClientData(db.Model):
    __tablename__ = "clientData"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(60), nullable = False)

class CreditData(db.Model):
    __tablename__ = "creditData"
    id = db.Column(db.Integer, primary_key=True)
    loanAmount = db.Column(db.Numeric(11,2), nullable = False)
    interestRate = db.Column(db.Numeric(4,2), nullable = False)

class InvestCreditData(db.Model):
    __tablename__ = "investCreditData"
    id = db.Column(db.Integer, primary_key=True)
    conclusionDate = db.Column(db.DateTime, nullable = False)
    conclusionPeriod = db.Column(db.Numeric(3), nullable = False)
    investmentValue = db.Column(db.Numeric(11,2), nullable = False)
    ownContribution = db.Column(db.Numeric(11,2), nullable = False)
    commission = db.Column(db.Numeric(4,2), nullable = False)
    repaymentScheduleType = db.Column(db.Enum(RepaymentScheduleType), nullable = False)
    clientData_id = db.Column(db.Integer, db.ForeignKey("clientData.id", ondelete='CASCADE'), nullable=False)
    creditData_id = db.Column(db.Integer, db.ForeignKey("creditData.id", ondelete='CASCADE'), nullable=False)
    clientData = db.relationship('ClientData', backref=db.backref('clientData_invest'))
    creditData = db.relationship('CreditData', backref=db.backref('creditData_invest'))

    @property
    def conclusionDateFormatted(self):
        return self.conclusionDate.strftime("%d.%m.%Y")

class AgroCreditData(db.Model):
    __tablename__ = "agroCreditData"
    id = db.Column(db.Integer, primary_key=True)
    conclusionDate = db.Column(db.DateTime, nullable = False)
    conclusionPeriod = db.Column(db.Numeric(3), nullable = False)
    clientData_id = db.Column(db.Integer, db.ForeignKey("clientData.id", ondelete='CASCADE'), nullable=False)
    creditData_id = db.Column(db.Integer, db.ForeignKey("creditData.id", ondelete='CASCADE'), nullable=False)
    repaymentScheduleType = db.Column(db.Enum(RepaymentScheduleType), nullable = False)
    clientData = db.relationship('ClientData', backref=db.backref('clientData'))
    creditData = db.relationship('CreditData', backref=db.backref('creditData'))

    @property
    def conclusionDateFormatted(self):
        return self.conclusionDate.strftime("%d.%m.%Y")