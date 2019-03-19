# Simple string reversing function using slicing. Asks for string, returns string in reverse. F strings
# requires Python 3.6 or higher

print('''
*******************************************************
             The Great String Reverser!!  
*******************************************************''')

def string_reverser (str):
    reversed=str[::-1]
    return reversed

reverse_me=input("Please enter a string you would like to reverse: ")

reversed_string=string_reverser(reverse_me)

print(f"Your reversed string is: {reversed_string}")