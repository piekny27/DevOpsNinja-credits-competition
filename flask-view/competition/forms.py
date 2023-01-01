from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, DecimalRangeField, DecimalField
from wtforms.validators import Length, DataRequired, InputRequired, NumberRange
from competition.enums import RepaymentScheduleType
from datetime import date

class AgroCreditForm(FlaskForm):
    fullname = StringField(label="Imię i nazwisko klienta / nazwa firmy", render_kw={"placeholder": "Imię i nazwisko klienta / nazwa firmy"}, validators=[DataRequired(), Length(min=3, max=60)])
    conclusionDate = DateField(label="Data zawarcia umowy", default= date.today(), validators=[DataRequired()])
    conclusionPeriod = DecimalRangeField(label = "Okres finansowania", render_kw={"step": "1"}, default=12, validators=[InputRequired(), NumberRange(min=1, max=24)]) #slider
    loanAmount = DecimalRangeField(label = "Kwota kredytu", render_kw={"step": "0.01"}, default=500, validators=[InputRequired(), NumberRange(min=500, max=150000.00)]) #slider
    interestRate = DecimalField(label = "Oprocentowanie kredytu", render_kw={"step": "0.01"}, default=2, validators=[InputRequired(), NumberRange(min=0, max=99.999)])
    repaymentScheduleType = SelectField(label="Typ harmonogramu spłat", choices=RepaymentScheduleType.choices(), coerce=RepaymentScheduleType.coerce, validators=[DataRequired()])
    submitBtn = SubmitField(label = "Pokaż podsumowanie")

class InvestCreditForm(FlaskForm):
    fullname = StringField(label="Imię i nazwisko klienta / nazwa firmy", render_kw={"placeholder": "Imię i nazwisko klienta / nazwa firmy"}, validators=[DataRequired(), Length(min=3, max=60)])
    conclusionDate = DateField(label="Data zawarcia umowy", default= date.today(), validators=[DataRequired()])
    conclusionPeriod = DecimalRangeField(label = "Okres finansowania", render_kw={"step": "1"}, default=12, validators=[InputRequired(), NumberRange(min=1, max=144)]) #slider
    investmentValue = DecimalRangeField(label = "Wartość inwestycji", render_kw={"step": "0.01"}, default=0, validators=[InputRequired(), NumberRange(min=0, max=999999999.99)]) #slider
    ownContribution = DecimalRangeField(label = "Wkład własny", render_kw={"step": "0.01"}, default=0, validators=[InputRequired(), NumberRange(min=0, max=999999999.99)]) #slider
    commission = DecimalField(label = "Prowizja", render_kw={"step": "0.01"}, default=2, validators=[InputRequired(), NumberRange(min=0, max=99.999)])
    loanAmount = DecimalRangeField(label = "Kwota kredytu", render_kw={"step": "0.01"}, default=500, validators=[InputRequired(), NumberRange(min=500, max=15000000.00)]) #slider
    interestRate = DecimalField(label = "Oprocentowanie kredytu", render_kw={"step": "0.01"}, default=7.03, validators=[InputRequired(), NumberRange(min=0, max=99.999)])
    repaymentScheduleType = SelectField(label="Typ harmonogramu spłat", choices=RepaymentScheduleType.choices(), coerce=RepaymentScheduleType.coerce, validators=[DataRequired()])
    submitBtn = SubmitField(label = "Pokaż podsumowanie")