ch = str(input("Enter an alphabet:"))
ch = ch.lower()
if ch >= 'a' and ch <= 'z':

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Entered alphabet is a Vowel")
    else:
        print("Entered alphabet is a Consonant")
else:    
    print("Entered character is not an alphabet.")
