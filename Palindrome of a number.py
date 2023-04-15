num=int(input("Enter any number:"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("Entered number is palindrome.")
else:
    print("Entered number is not a palindrome.")
    
