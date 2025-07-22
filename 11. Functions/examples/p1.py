# Write a program using functions to check if a string is palindrome or not

def is_Palindrome(text):
    rev_text = text[::-1]
    if(text == rev_text):
        return("Palindrome")
    else:
        return("Not a Palindrome")
    
org_text = input("Enter the text to check: ").lower()
result = is_Palindrome(org_text)
print(result)