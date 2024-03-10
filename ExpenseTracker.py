class Expense:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        expense = Expense(category, description, amount)
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        total_expenses = 0
        print("Expenses:")
        for i, expense in enumerate(self.expenses, 1):
            total_expenses += expense.amount
            print(f"{i}. Category: {expense.category}, Description: {expense.description}, Amount: ${expense.amount}")
        print(f"Total Expenses: ${total_expenses}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: $"))
            expense_tracker.add_expense(category, description, amount)
            print("Expense added successfully.")
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
