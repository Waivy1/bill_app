import webbrowser

from fpdf import FPDF


class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.perion = period


class Flatmate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, person2):

        weight = int(self.days_in_house) / (self.days_in_house + person2.days_in_house)
        return weight * int(bill.amount)


class PDFReport:

    def __init__(self, filename):
        self.filename = filename

    def create_file(self, person1, person2, bill):

        person1_pay = str(round(person1.pays(bill, person2), 2))
        person2_pay = str(round(person2.pays(bill, person1), 2))

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 22)
        pdf.cell(40, 10, 'bill', ln=1)

        pdf.cell(100, 30, 'period:', ln=1)
        pdf.cell(150, 30, bill.perion, ln=1)

        pdf.cell(100, 20, person1.name, ln=1)
        pdf.cell(150, 20, person1_pay)

        pdf.cell(100, 20, person2.name, ln=1)
        pdf.cell(150, 20, person2_pay)

        pdf.output(f'{self.filename}.pdf', 'F')

        # webbrowser.open(self.filename)


bill_amount = input('enter a bill amount:')
period = input('enter a month: ')

first_person_name = input('enter a first person name: ')
first_person_days = int(input('enter amount of days: '))


second_person_name = input('enter a second person name: ')
second_person_days = int(input('enter amount of days: '))

the_bill = Bill(amount=bill_amount, period=period)
first_person = Flatmate(first_person_name, first_person_days)
second_person = Flatmate(second_person_name, second_person_days)

print(first_person.name, first_person.pays(the_bill, second_person))

pdf_report = PDFReport('report3.pdf')
pdf_report.create_file(first_person, second_person, the_bill)