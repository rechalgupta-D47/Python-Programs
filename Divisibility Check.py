x=int(input("Enter a number:"))
d1=int(input("Enter first divisor:"))
d2=int(input("Enter second divisor:"))
if x%d1==0 and x%d2==0:
    print("Entered number is divisible by both the divisors")
elif x%d1!=0 or x%d2!=0:
    print("Entered number is not divisible by either or both of the divisors")
