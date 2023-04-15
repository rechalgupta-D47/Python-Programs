x=int(input("Enter first value:"))
y=int(input("Enter second value:"))
sum=0
print("List of even numbers in entered range:")
if x<y:
    for i in range(x,(y+1),2):
        if i%2==0:
            print(i)
            sum=sum+i
elif x>y:
    for i in range(y,(x+1),2):
        if i%2==0:
            print(i)
            sum=sum+i
print("Sum of even numbers in entered range:",sum)
