import re
from datetime import datetime
from category_list import CategoryList
from storage import StorageManager

class ExpenseManager:
    def __init__(self):
        """
        Initialize the ExpenseManager with default attributes.
        """
        self.description = None
        self.amount = None
        self.category = None
        self.date = None
        self.categories = CategoryList(export_key=self)  # Initialize CategoryList with export_key
        self.storage_manager = StorageManager()

    def expense_output(self):
        """
        Output the details of the added expense.
        """
        if all([self.description, self.amount, self.category, self.date]):
            print("\n=== Expense Added Successfully ===")
            print(f"Description: {self.description}")
            print(f"Amount: ${self.amount:.2f}")
            print(f"Category: {self.category}")
            print(f"Date: {self.date}")
            print("===============================")
        else:
            print("Incomplete expense details. Please try again.")
    
    def description_validation(self):
        """
        Validate the expense description.
        Description must be alphabetic, 3–50 characters long, and can include underscores or hyphens.
        """
        pattern = r'^[A-Za-z][A-Za-z_-]*[A-Za-z]$'
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            description = input("Enter expense description (alphabetic, 3–50 characters): ").strip()
            if re.match(pattern, description) and 3 <= len(description) <= 50:
                return description
            else:
                print("Invalid description format:")
                print("[1] Must be alphabetic (minimum 3 characters).")
                print("[2] Can include underscores or hyphens.")
                print("[3] Maximum length is 50 characters.")
            attempts += 1

        raise ValueError("Too many invalid attempts for description validation.")

    def amount_validation(self):
        """
        Validate the expense amount.
        Amount must be a non-negative integer.
        """
        max_attempts = 3  # Maximum number of retries
        attempts = 0
        while attempts < max_attempts:
            try:
                amount = int(input("Enter the amount spent: "))
                if amount >= 0:
                    return amount
                else:
                    print("Amount must be a non-negative integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            attempts += 1
        raise ValueError("Too many invalid attempts for amount validation.")
    
    def date_validation(self):
        """
        Validate the expense date.
        Date must be in the format YYYY-MM-DD, cannot be a future date, and must be after 2000-01-01.
        """
        max_attempts = 3
        attempts = 0
        date_format = "%Y-%m-%d"
        current_date = datetime.now().date()
        min_date = datetime(2000, 1, 1).date()  # Earliest valid date

        while attempts < max_attempts:
            date_input = input("Enter the date of the expense (YYYY-MM-DD): ").strip()
            try:
                parsed_date = datetime.strptime(date_input, date_format).date()
                if parsed_date > current_date and parsed_date >= min_date:
                    print("Error: Cannot add expenses for future dates. Please enter a valid past or present date.")
                elif parsed_date < min_date:
                    print("Error: Date must be after 2000-01-01.")
                else:
                    return parsed_date.strftime(date_format)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
            attempts += 1

        raise ValueError("Too many invalid attempts for date validation.")
    
    def select_top_level_category(self):
        """
        Allow the user to select a top-level category interactively.
        :return: The selected top-level category name.
        """
        print("\nSelect a Top-Level Category:")
        top_level_categories = self.categories.display_top_level_categories()

        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                choice = int(input("Enter the number of the top-level category: "))
                selected_category = self.categories.get_category_by_index(top_level_categories, choice)
                if selected_category:
                    print(f"You selected: {selected_category}")
                    return selected_category
                else:
                    print("Invalid choice. Please select a valid top-level category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            attempts += 1
        raise ValueError("Too many invalid attempts for top-level category selection.")
    
    def select_subcategory(self, top_level_category):
        """
        Allow the user to select a subcategory under a top-level category.
        :param top_level_category: The name of the top-level category.
        :return: The selected subcategory name.
        """
        print(f"\nSelect a Subcategory under '{top_level_category}':")
        subcategories = self.categories.display_subcategories(top_level_category)

        while True:
            try:
                choice = int(input("Enter the number of the subcategory: "))
                selected_subcategory = self.categories.get_category_by_index(subcategories, choice)
                if selected_subcategory:
                    print(f"You selected: {selected_subcategory}")
                    return selected_subcategory
                else:
                    print("Invalid choice. Please select a valid subcategory number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_category(self):
        """
        Allow the user to select a category interactively.
        :return: A string representing the full category path (e.g., "Food > Groceries").
        """
        # Step 1: Select a top-level category
        top_level_category = self.select_top_level_category()

        # Step 2: Select a subcategory
        subcategory = self.select_subcategory(top_level_category)

        # Return the full category path
        return f"{top_level_category} > {subcategory}"

    def display(self):
        """
        Collect and validate all expense details.
        """
        self.description = self.description_validation()
        self.amount = self.amount_validation()
        self.category = self.select_category()
        self.date = self.date_validation()

    def add_expense(self):
        """
        Add an expense by collecting and validating details.
        """
        print("\n=== Add a New Expense ===")
        self.display()
        self.expense_output()
        self.storage_manager.save_expense(
            self.description,
            self.amount,
            self.category,
            self.date
        )


if __name__ == "__main__":
    expense = ExpenseManager()
    expense.add_expense()