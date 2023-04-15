a = input("Enter a string to check palindrome:")
a = a.upper()
b = a[::-1]
if b == a:
    print("Entered string is palindrome.")
else:
    print("Entered string is not palindrome")
print(a)
