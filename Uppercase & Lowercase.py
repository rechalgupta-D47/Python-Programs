ch = input("Enter any character:")
if ch >= 'a' and ch <= 'z':
    print("Entered character is in Lowercase.")
elif ch >= 'A' and ch <= 'Z':
    print("Entered character is in Uppercase.")
elif ch >= '0' and ch <= '9':
    print("Entered character is Digit.")
else:
    print("Entered character is invalid")