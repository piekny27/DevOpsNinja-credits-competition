from marshmallow import Schema, fields
from competition.enums import RepaymentScheduleType

class CreditDataSchema(Schema):
    id = fields.Int(dump_only=True)
    loanAmount = fields.Str()
    interestRate = fields.Str()

class ClientDataSchema(Schema):
    id = fields.Int(dump_only=True)
    fullname = fields.Str()

class AgroCreditDataSchema(Schema):
    id = fields.Int()
    conclusionDate = fields.Date(format='%d.%m.%Y')
    conclusionPeriod = fields.Str()
    repaymentScheduleType = fields.Enum(RepaymentScheduleType, by_value = True)
    clientData = fields.Nested(ClientDataSchema)
    creditData = fields.Nested(CreditDataSchema)

class InvestCreditDataSchema(Schema):
    id = fields.Int()
    conclusionDate = fields.Date(format='%d.%m.%Y')
    conclusionPeriod = fields.Str()
    investmentValue = fields.Str()
    ownContribution = fields.Str()
    commission = fields.Str()
    repaymentScheduleType = fields.Enum(RepaymentScheduleType, by_value = True)
    clientData = fields.Nested(ClientDataSchema)
    creditData = fields.Nested(CreditDataSchema)