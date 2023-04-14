num=int(input("Enter any number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(i,fact)
print("Factorial of entered number:",fact)