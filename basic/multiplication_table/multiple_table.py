class Multiply:
    def __init__(self):
        self.user_value = None
        self.user_range = 10

    def table_generate(self, user_input, user_range):
        # Generate the multiplication table
        for element in range(0, user_range + 1):
            print(f"{user_input} x {element} = {user_input * element}")

    def user_range_validation(self):
        # Validate the range input
        while True:
            try:
                user_range = int(input("[OPTIONAL] Enter the range of the table greater than 10.\nIf not enter '0' -> "))
                if user_range > self.user_range:
                    return user_range
                elif user_range == 0:
                    return self.user_range
                else:
                    print("Invalid range value, Please try again!")
            except ValueError:
                print("Invalid value")

    def user_validation(self):
        # Validate the integer input
        while True:
            try:
                user_input = int(input("Enter the Integer value of the table -> "))
                if user_input > 0:
                    return user_input
                else:
                    print("Invalid Integer, Please try again!")
            except ValueError:
                print("Invalid value")

    def table(self):
        # Main method to execute the program
        print("======================================")
        print("Welcome to the Math Tables!")
        print("======================================")
        self.user_value = self.user_validation()
        self.user_range = self.user_range_validation()
        self.table_generate(self.user_value, self.user_range)


if __name__ == "__main__":
    value = Multiply()
    value.table()