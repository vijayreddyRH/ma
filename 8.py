# Parent class
class PalindromeChecker:
 def __init__(self, input_str):
 self.input_str = input_str
 
 def is_palindrome(self):
 pass
class StringPalindromeChecker(PalindromeChecker):
 def __init__(self, input_str):
 super().__init__(input_str)
 
 def is_palindrome(self):
 reversed_str = self.input_str[::-1]
 return self.input_str.lower() == reversed_str.lower()
class IntegerPalindromeChecker(PalindromeChecker):
def __init__(self, input_int):
 super().__init__(str(input_int))
 
 def is_palindrome(self):
 reversed_str = self.input_str[::-1]
 return self.input_str == reversed_str
user_input = input("Enter a string or number to check palindromicity: ")
str_palindrome = StringPalindromeChecker(user_input)
if str_palindrome.is_palindrome():
 print("The entered string is a palindrome.")
else:
 print("The entered string is not a palindrome.")
try:
 int_input = int(user_input)
 int_palindrome = IntegerPalindromeChecker(int_input)
 if int_palindrome.is_palindrome():
 print("The entered number is a palindrome.")
 else:
 print("The entered number is not a palindrome.")
except ValueError:
 pass
