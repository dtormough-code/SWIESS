"""
budget_tracker.py
--------------------
The main program the user interacts with: a menu-driven CLI.
All actual data handling is delegated to the BudgetTracker class
in model.py - this file only handles user input/output.
"""

from datetime import datetime
from model import BudgetTracker

tracker = BudgetTracker()
tracker.load()  # load any previously saved data when the program starts


def get_valid_amount(prompt):
    """Keep asking until the user enters a valid, positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
        except ValueError:
            print("That's not a valid number. Please enter digits only.\n")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.\n")
            continue
        return amount


def get_valid_category():
    """Keep asking until the user enters a non-empty category."""
    while True:
        category = input("Enter category (e.g. food, rent, salary): ").strip()
        if category == "":
            print("Category cannot be empty.\n")
            continue
        return category


def add_income():
    """Ask the user for income details, add it, and save."""
    amount = get_valid_amount("Enter income amount: ")
    category = get_valid_category()
    now = datetime.now()
    tracker.add_income(amount, category, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))
    tracker.save()
    print("Income added and saved.\n")


def add_expense():
    """Ask the user for expense details, add it, and save."""
    amount = get_valid_amount("Enter expense amount: ")
    category = get_valid_category()
    now = datetime.now()
    tracker.add_expense(amount, category, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))
    tracker.save()
    print("Expense added and saved.\n")


def delete_expense():
    """Let the tracker handle expense deletion, then save the change."""
    tracker.delete_expense()
    tracker.save()


def view_balance():
    """Show income/expense/balance totals, then pause so it's readable."""
    tracker.view_balance()
    input("\nPress Enter to continue...")


def view_transactions():
    """Show full transaction history, then pause so it's readable."""
    tracker.view_transactions()
    input("\nPress Enter to continue...")


def view_spending_by_category():
    """Show spending grouped by category, then pause so it's readable."""
    tracker.view_spending_by_category()
    input("\nPress Enter to continue...")


def set_budget_limit():
    """Ask for a new budget limit, set it, and save."""
    amount = get_valid_amount("Enter your budget limit: ")
    tracker.set_budget_limit(amount)
    tracker.save()


def main():
    """Run the main menu loop until the user chooses to exit."""
    menu = """
==== BUDGET TRACKER (OOP version) ====
1. Add income
2. Add expense
3. Delete expense
4. View balance
5. View transaction history
6. View spending by category
7. Set budget limit
8. Exit
========================================
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            view_balance()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            view_spending_by_category()
        elif choice == "7":
            set_budget_limit()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()