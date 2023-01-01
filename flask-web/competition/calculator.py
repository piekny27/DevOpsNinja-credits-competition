from dateutil import relativedelta
from decimal import Decimal
from competition.models import  CreditScheduleEntry
from competition.enums import RepaymentScheduleType

class ScheduleCalculator:
    def __init__(self, creditData): 
        if creditData.repaymentScheduleType == RepaymentScheduleType.MONTHLY:
            self.installmentsInYear = Decimal(12)
            self.installmentCount = creditData.conclusionPeriod
        elif creditData.repaymentScheduleType == RepaymentScheduleType.QUATERLY:
            self.installmentsInYear = Decimal(4)
            self.installmentCount = creditData.conclusionPeriod / 3
        self.amount = creditData.creditData.loanAmount 
        self.repaymentScheduleType = creditData.repaymentScheduleType
        self.interestRate = creditData.creditData.interestRate
        self.conclusionDate = creditData.conclusionDate

    def calculate(self):
        singleInstallment = self.singleInstallmenta(self.amount, self.installmentCount, self.interestRate)
        entries = []
        capitalLeftToPay = self.amount
        paymentDate = self.calculateNextPaymentDate(self.conclusionDate)

        for i in range(int(self.installmentCount)):
            interest = self.calculateInterest(capitalLeftToPay, self.interestRate)
            capital = Decimal(singleInstallment - interest)
            capitalLeftToPay = Decimal(capitalLeftToPay - capital)
            entries.append(CreditScheduleEntry(paymentDate, capital, interest, singleInstallment))
            paymentDate = self.calculateNextPaymentDate(paymentDate)
        return entries

    def calculateInterest(self, leftToPay, interestRate):
        interest = interestRate / Decimal(100)
        numerator = Decimal(leftToPay) * interest
        return Decimal(numerator / self.installmentsInYear)

    def calculateNextPaymentDate(self, date):
        match self.repaymentScheduleType:
            case RepaymentScheduleType.MONTHLY:
                return date + relativedelta.relativedelta(months=1)
            case RepaymentScheduleType.QUATERLY:
                return date + relativedelta.relativedelta(months=3)

    def singleInstallmenta(self, amount, installmentCount, interestRate):
        if interestRate == 0:
            return Decimal(amount / installmentCount)
        interest = interestRate / Decimal(100)
        installmentsInYear = self.installmentsInYear
        numerator = amount * interest
        growingInterest = pow(installmentsInYear / (installmentsInYear + interest), installmentCount)
        divider = installmentsInYear * (1-growingInterest)
        return Decimal(numerator / divider)
