"""
model.py
----------
Defines the data model for the Budget Tracker:
- Expense: a single money-out transaction
- Income: a single money-in transaction
- BudgetTracker: manages a collection of transactions, handles
  balance/history/category views, and saves/loads via utils.py
"""

from utlis import load_data, save_data


class Expense:
    """Represents a single expense transaction."""

    def __init__(self, amount, category, date, time):
        """Store the amount, category, date, and time of this expense."""
        self.amount = amount
        self.category = category
        self.date = date
        self.time = time

    def to_dict(self):
        """Convert this Expense into a plain dictionary for JSON saving."""
        return {
            "type": "expense",
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "time": self.time,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild an Expense object from a dictionary loaded from JSON."""
        return cls(data["amount"], data["category"], data["date"], data["time"])


class Income:
    """Represents a single income transaction."""

    def __init__(self, amount, category, date, time):
        """Store the amount, category, date, and time of this income."""
        self.amount = amount
        self.category = category
        self.date = date
        self.time = time

    def to_dict(self):
        """Convert this Income into a plain dictionary for JSON saving."""
        return {
            "type": "income",
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "time": self.time,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild an Income object from a dictionary loaded from JSON."""
        return cls(data["amount"], data["category"], data["date"], data["time"])


class BudgetTracker:
    """Manages a list of Income/Expense transactions and a budget limit."""

    def __init__(self):
        """Start with an empty transaction list and no budget limit set."""
        self.transactions = []
        self.budget_limits = None

    def add_expense(self, amount, category, date, time):
        """Create a new Expense and add it to the transaction list."""
        expense = Expense(amount, category, date, time)
        self.transactions.append(expense)

    def add_income(self, amount, category, date, time):
        """Create a new Income and add it to the transaction list."""
        income = Income(amount, category, date, time)
        self.transactions.append(income)

    def view_balance(self):
        """Print total income, total expenses, and the net balance."""
        total_expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        print(f"Total Expenses: {total_expenses}")
        print(f"Total Income: {total_income}")
        print(f"Net Balance: {total_income - total_expenses}")

    def view_transactions(self):
        """Print every transaction with its index, so the user can reference it later (e.g. to delete)."""
        if not self.transactions:
            print("No transactions found.")
            return
        for i, t in enumerate(self.transactions):
            t_type = "Income" if isinstance(t, Income) else "Expense"
            print(f"{i}: {t.date} {t.time} - {t_type}: {t.category}: {t.amount}")

    def set_budget_limit(self, amount):
        """Set the budget limit for this tracker."""
        self.budget_limits = amount
        print(f"Budget limit set to {amount}.")

    def delete_expense(self):
        """List expenses only, ask the user which one to delete, and remove it."""
        expenses = [t for t in self.transactions if isinstance(t, Expense)]

        if not expenses:
            print("No expenses to delete.")
            return

        for i, t in enumerate(expenses):
            print(f"{i}: {t.date} {t.time} - {t.category}: {t.amount}")

        try:
            index = int(input("Enter the index of the expense to delete: "))
        except ValueError:
            print("That's not a valid number.")
            return

        if 0 <= index < len(expenses):
            expense_to_delete = expenses[index]
            self.transactions.remove(expense_to_delete)
            print(f"Deleted: {expense_to_delete.category} - {expense_to_delete.amount}")
        else:
            print("Invalid index.")

    def view_spending_by_category(self):
        """Print total expense spending, grouped by category."""
        category_totals = {}
        for t in self.transactions:
            if isinstance(t, Expense):
                category_totals[t.category] = category_totals.get(t.category, 0) + t.amount

        if not category_totals:
            print("No expenses found.")
            return

        for category, total in category_totals.items():
            print(f"Category: {category}, Total Spending: {total}")

    def save(self):
        """Convert all transactions to dictionaries and save them via utils.py."""
        transactions_as_dicts = [t.to_dict() for t in self.transactions]
        save_data({"transactions": transactions_as_dicts, "budget_limit": self.budget_limits})

    def load(self):
        """Load saved data via utils.py and rebuild Income/Expense objects from it."""
        data = load_data()
        self.budget_limits = data["budget_limit"]
        self.transactions = []
        for t_dict in data["transactions"]:
            if t_dict["type"] == "income":
                self.transactions.append(Income.from_dict(t_dict))
            else:
                self.transactions.append(Expense.from_dict(t_dict))


if __name__ == "__main__":
    # Simple manual test - only runs when this file is executed directly,
    # not when it's imported by budget_tracker.py
    tracker = BudgetTracker()
    tracker.add_expense(2000, "food", "2023-10-01", "14:30")
    tracker.add_income(5000, "salary", "2023-10-01", "09:00")
    tracker.view_balance()
    tracker.view_transactions()
    tracker.set_budget_limit(10000)
    tracker.view_spending_by_category()