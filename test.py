class Expense:
    def __init__(self, amount, category, date, time):
        self.amount = amount
        self.category = category
        self.date = date
        self.time = time

    def to_dict(self):
        return {
            "type": "expense",
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "time": self.time
        }