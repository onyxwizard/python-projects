class Application:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.report_generator = ReportGenerator()
    
    def display_menu(self):
        """Displays the main menu options."""
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Monthly Report")
        print("3. Exit")
        print("=== --------------- ===")
    
    def get_user_choice(self):
        """Prompts the user for their choice and validates it."""
        while True:
            try:
                choice = input("Enter your choice: ")
                if choice in ['1', '2', '3']:
                    return choice
                else:
                    print(f"Invalid Selection of choice -> {choice}")
            except ValueError:
                print("Invalid choice. Please try again.")
    
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
                    print("Exiting...")
                    break

if __name__ == "__main__":
    app = Application()  # Create an instance of the Application class
    app.run()  # Run the application