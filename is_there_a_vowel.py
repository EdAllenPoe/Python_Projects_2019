# Simple function to count vowels in a phrase entered by user. Uses ".lower" string method to convert 
# capital vowels for counting. F string interpolation for Python 3.6 or higher.  Conditional statement
# to iterate through input phrase and match against a local list of vowels.

print('''
*******************************************************
      The Greatest Vowel Counter Function EVER!!  
*******************************************************''')

def vowel_finder(phrase):
    vowels=["a","e","i","o","u"]
    total_vowels=0
    for i in phrase.lower():
        if i in vowels:
            total_vowels+=1
    return total_vowels

your_phrase=input("Give me a phrase so i can count the vowels: ")

vowel_count=vowel_finder(your_phrase)

print(f"There are {vowel_count} vowels in your phrase")