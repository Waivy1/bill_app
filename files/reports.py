from fpdf import FPDF


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