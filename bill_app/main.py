from bill_app.person import Bill, Flatmate
from bill_app.reports import PDFReport

bill_amount = input('enter a bill amount:')
period = input('enter a month: ')

first_person_name = input('enter a first person name: ')
first_person_days = int(input(f'enter amount of days for {first_person_name}: '))


second_person_name = input('enter a second person name: ')
second_person_days = int(input(f'enter amount of days for {second_person_name}: '))

the_bill = Bill(amount=bill_amount, period=period)
first_person = Flatmate(first_person_name, first_person_days)
second_person = Flatmate(second_person_name, second_person_days)

print(first_person.name, first_person.pays(the_bill, second_person))

pdf_report = PDFReport(f'{the_bill.perion}.pdf')
pdf_report.create_file(first_person, second_person, the_bill)