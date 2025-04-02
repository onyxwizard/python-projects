import re
class ExpenseManager():
    
    def __init__(self):
        self.description = None
        self.amount = None
        self.category = None
    
    def expense_output(self):
        pass
    
    def description_validation(self):
        pattern = r'^[A-Za-z][A-Za-z_-]+[A-Za-z]$'
        while True:
            try:
                description = input("Enter expense description: ").strip()  # Strip whitespace
                if re.match(pattern,description) and len(description) <= 15:
                    return description
                else:
                    print(f"Invalid description format. Need to be Alphabets and under 15 characters")
            except ValueError:
                print("Invalid Input value")
                
    
    def category_validation(self):
        pass
    
    def amount_validation(self):
        pass
    
    def display(self):
        self.description = self.description_validation()
        print("Enter expense amount: ")
        amount = self.amount_validation()
        print("Enter expense category: ")
        category = self.category_validation()
        # Expense added: Groceries, $100.00, Category: Food
    
    def add_expense(self):
        self.display()
        
if __name__ == "__main__":
    expense = ExpenseManager()
    expense.add_expense()