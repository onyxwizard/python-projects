class Palindrome:
    def __init__(self):
        self.user_input = None
        self.reverse_result = None
    
    def string_palindrome(self,user_input) -> bool:
        # In-place checking
        left,right = 0,len(user_input)-1
        while left<right:
            if user_input[left] != user_input[right]:
                return False
            left+=1
            right-=1
        return True
    
    def integer_palindrome(self,user_input) -> bool:
        reverse_result = 0
        while user_input > 0:
            reverse_result = (reverse_result * 10) + (user_input % 10)
            user_input = user_input // 10
        return bool(reverse_result == self.user_input)
        
    def string_validation(self) -> str:
        while True:
            try:
                user_input = input("Enter the string value -> ")
                if user_input.isalpha():
                    return user_input  # input() always returns a string
            except Exception:
                print("Invalid input. Please enter a valid string.")
            
    def integer_validation(self)-> int:
        while True:
            try:
                user_input = int(input("Enter the integer value -> "))
                if user_input > 0:
                    return user_input
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
                
    def choice_validation(self,choice):
        if choice == 1:
            return self.string_validation()
        else:
            return self.integer_validation()
    
    def choice(self):
        while True:
            try:
                user_choice = int(input("Check Palindrome for\n1:String\n2:Integer -> "))
                print("======================================")
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
        user_choice = self.choice()
        self.user_input = self.choice_validation(user_choice)
        if user_choice == 1:
            self.reverse_result = self.string_palindrome(self.user_input)
        else:
            self.reverse_result = self.integer_palindrome(self.user_input)
        
        if self.reverse_result:
            print("The Given value is a palindrome")
        else:
            print("Not a palindrome")
        print("======================================")
            
    
if __name__ == "__main__":
    value = Palindrome()
    value.checker()