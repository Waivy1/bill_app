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