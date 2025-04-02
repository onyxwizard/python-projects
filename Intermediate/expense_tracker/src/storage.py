import csv
import os


class StorageManager:
    def __init__(self, file_path="../data/expenses.csv"):
        """
        Initialize the StorageManager with the file path for storing expenses.
        """
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Ensure the CSV file exists. If not, create it with headers.
        """
        if not os.path.exists("data"):
            os.makedirs("data")  # Create the 'data' directory if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Description", "Amount", "Category", "Date"])  # Write headers

    def save_expense(self, description, amount, category, date):
        """
        Save an expense to the CSV file in append mode.
        """
        with open(self.file_path, "a", newline="") as file:  # Use append mode ("a")
            writer = csv.writer(file)
            writer.writerow([description, amount, category, date])

    def load_expenses(self):
        """
        Load all expenses from the CSV file.
        :return: A list of dictionaries representing expenses.
        """
        expenses = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(row)
        return expenses