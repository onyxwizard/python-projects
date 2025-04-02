from storage import StorageManager

class ReportGenerator:
    def __init__(self, storage_manager=None):
        """
        Initialize the ReportGenerator with a StorageManager instance.
        :param storage_manager: An instance of StorageManager for loading expenses.
        """
        self.storage_manager = storage_manager or StorageManager()

    def load_expenses(self):
        """
        Load expenses from storage.
        :return: A list of expense dictionaries, or None if no expenses are found.
        """
        expenses = self.storage_manager.load_expenses()
        if not expenses:
            print("No expenses found.")
            return None
        return expenses

    def process_expenses(self, expenses):
        """
        Process expenses to group them by month and category.
        :param expenses: A list of expense dictionaries.
        :return: A dictionary mapping months to categories and their totals.
        """
        monthly_totals = {}
        for expense in expenses:
            date = expense["Date"]
            year_month = date[:7]  # Extract YYYY-MM
            category = expense["Category"]
            amount = float(expense["Amount"])

            if year_month not in monthly_totals:
                monthly_totals[year_month] = {}
            if category not in monthly_totals[year_month]:
                monthly_totals[year_month][category] = 0
            monthly_totals[year_month][category] += amount

        return monthly_totals

    def format_report(self, monthly_totals):
        """
        Format the processed data into a readable report structure.
        :param monthly_totals: A dictionary mapping months to categories and their totals.
        :return: A formatted string representing the report.
        """
        report = ["\n=== Monthly Expense Report ==="]
        for year_month, categories in monthly_totals.items():
            report.append(f"\nMonth: {year_month}")
            for category, total in categories.items():
                report.append(f"  {category}: ${total:.2f}")
            report.append(f"Total for {year_month}: ${sum(categories.values()):.2f}")
        return "\n".join(report)

    def display_report(self, report):
        """
        Display the report to the user.
        :param report: A formatted string representing the report.
        """
        print(report)

    def generate_report(self):
        """
        Generate and display a monthly expense report.
        """
        # Step 1: Load expenses
        expenses = self.load_expenses()
        if not expenses:
            return

        # Step 2: Process expenses
        monthly_totals = self.process_expenses(expenses)

        # Step 3: Format the report
        formatted_report = self.format_report(monthly_totals)

        # Step 4: Display the report
        self.display_report(formatted_report)