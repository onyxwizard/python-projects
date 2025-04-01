class Palindrome:
    def __init__(self):
        self.user_choice = None
        self.user_input = None
        self.reverse_result = None
    
    def string_palindrome(self,user_input) -> str:
        # In-place checking
        left,right = 0,len(user_input)-1
        while left<right:
            if user_input[left] != user_input[right]:
                self.reverse_result = False
                return self.reverse_result
            left+=1
            right-=1
        self.reverse_result = True
        return self.reverse_result
    
    def integer_palindrome(self,user_input) -> int:
        pass
        
    def string_validation(self) -> str:
        while True:
            try:
                user_input = str(input("Enter the string value -> "))
                if type(user_input) is str:
                    return user_input
                else:
                    print("Invalid Data Type ")
            except ValueError:
                print("Invalid input. Please enter a valid String.")
            
    def integer_validation(self)-> int:
        while True:
            try:
                user_input = int(input("Enter the Integer value -> "))
                if type(user_input) is int:
                    return user_input
                else:
                    print("Invalid Data Type ")
            except ValueError:
                print("Invalid input. Please enter a valid Integer.")
    
                
    def choice_validation(self,choice):
        if choice == 1:
            return self.string_validation()
        else:
            return self.integer_validation()
    
    def choice(self):
        while True:
            try:
                user_choice = int(input("Check Palindrome for\n1:String\n2:Integer -> "))
                if 1<= user_choice <=2:
                    return user_choice
                else:
                    print("Invalid choice selection")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def checker(self):
        print("======================================")
        print("Welcome to the Palindrome Checker!")
        print("======================================")
        self.user_choice = self.choice()
        self.user_input = self.choice_validation(self.user_choice)
        if self.user_choice == 1:
            self.user_input = self.string_palindrome(self.user_input)
        else:
            self.user_input = self.integer_palindrome(self.user_input)
        
        if self.reverse_result or self.reverse_result == self.user_input:
            print("The Given value is a palindrome")
        else:
            print("Not a palindrome")
            
    
if __name__ == "__main__":
    value = Palindrome()
    value.checker()