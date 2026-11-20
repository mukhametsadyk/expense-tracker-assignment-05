class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        expense = {
            "category": category.strip(),
            "amount": float(amount),
        }
        self.expenses.append(expense)
        return expense

    def total_amount(self):
        return sum(item["amount"] for item in self.expenses)

    def total_by_category(self, category):
        target = category.strip().lower()
        return sum(
            item["amount"]
            for item in self.expenses
            if item["category"].lower() == target
        )

    def remove_expense(self, index):
        return self.expenses.pop(index)