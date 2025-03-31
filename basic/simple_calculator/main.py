class Calculator:
    # def __init__(self):
    #     self.user_input
    #     self.arithmetic_operation
    
    def arithmetic(self,ops,val1,val2):
        operation = {
            1:self.addition(val1,val2),
            2:self.subtraction(val1,val2),
            3:self.multiple(val1,val2),
            4:self.division(val1,val2),
            5: self.exponentiation(val1, val2),
        }
        return operation.get(ops, "Invalid Operation")
    
    def user_selection(self):
        while True:
            try:
                ops = int(input("Operation -> "))
                if 1<= ops <=5:
                    return ops
                else:
                    print("Invalid Input. Try Again")
            except ValueError:
                print("Invalid")

    def addition(self,val1,val2):
        return val1 + val2
    
    def subtraction(self,val1,val2):
        return val1 - val2
    
    def multiple(self,val1,val2):
        return val1 * val2
    
    def division(self,val1,val2):
        try:
            return val1 / val2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    
    def exponentiation(self, val1, val2):
        return val1 ** val2
    
    def user_choice(self):
        print("======================================")
        print("Welcome to the Calculator App!")
        print("======================================")
        while True:
            try:
                # Get two numbers from the user
                print("Enter Two Values (separated by space):")
                val1, val2 = map(float, input().split())
                
                # Display available operations
                print("======================================")
                print("Select the Operation:")
                print("--------------------------------------")
                print("1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exponentiation")
                print("======================================")
                
                # Get user-selected operation
                choice = self.user_selection()
                
                # Perform calculation and display result
                result = self.arithmetic(choice, val1, val2)
                print(f"Result: {result}")
                
                # Ask if the user wants to perform another calculation
                repeat = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
                if repeat not in ["yes", "y"]:
                    print("Thank you for using the Calculator App!")
                    break
            except ValueError:
                print("Invalid Input. Please enter exactly two numeric values separated by a space.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    cal  = Calculator()
    cal.user_choice()