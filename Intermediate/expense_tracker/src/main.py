from input_handler import ExpenseManager
from reports import ReportGenerator
from visualizations import VisualizationManager


class Application:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.report_generator = ReportGenerator()
        self.visualization_manager = VisualizationManager()  # Add VisualizationManager instance
    
    def display_menu(self):
        """Displays the main menu options."""
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Monthly Report")
        print("3. Visualize Expenses")  # New option for visualization
        print("4. Exit")
        print("=== --------------- ===")
    
    def get_user_choice(self):
        """Prompts the user for their choice and validates it."""
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            choice = input("Enter your choice: ")
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print(f"Invalid Selection of choice -> {choice}")
                attempts += 1
        raise ValueError("Too many invalid attempts for menu selection.")
    
    def run(self):
        """Runs the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice == '1':
                self.expense_manager.add_expense()
            elif choice == '2':
                self.report_generator.generate_report()
            elif choice == '3':
                self.visualization_manager.visualize_expenses()  # Call the refactored visualize_expenses method
            elif choice == '4':
                print("Exiting...")
                break

    def visualize_expenses(self):
        """Visualize expenses using the VisualizationManager."""
        print("\n=== Visualizing Expenses ===")
        self.visualization_manager.visualize_expenses()


if __name__ == "__main__":
    app = Application()  # Create an instance of the Application class
    app.run()  # Run the application