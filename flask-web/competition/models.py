class CreditScheduleEntry:
    def __init__(self, paymentDate, capital, interest ,installment): 
        self.paymentDate = paymentDate.strftime("%d.%m.%Y")
        self.capital = format(capital, ".2f")
        self.interest = format(interest, ".2f")
        self.installment = format(installment, ".2f")

class CreditSchedule:
    def __init__(self):
        self.entries = []
    
