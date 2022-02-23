from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from bill_app.person import Flatmate, Bill

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form,
                               )

    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        the_bill = Bill(amount, period)

        name1 = billform.name1.data
        days = billform.days_in_the_house.data

        name2 = billform.name2.data
        days2 = billform.days_in_the_house2.data

        person1 = Flatmate(name1, days)
        person2 = Flatmate(name2, days2)

        return render_template('bill_form_page.html',
                               result=True,
                               billform=billform,
                               name1=name1, name2=name2,
                               amount1=person1.pays(the_bill, person2),
                               amount2=person2.pays(the_bill, person1)
                               )


class BillForm(Form):
    amount = StringField('bill amount: ', default=120)
    period = StringField('bill period: ', default='none')

    name1 = StringField('name: ', default='vi')
    days_in_the_house = StringField('days_in_the_house: ', default=30)

    name2 = StringField('name of second person: ', default='di')
    days_in_the_house2 = StringField('days_in_the_house: ', default=30)

    button = SubmitField('calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))


app.run(debug=True)
