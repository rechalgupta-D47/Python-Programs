num=int(input("Enter a number:"))
temp=num
count=0
while num:
    i=1
    fact=1
    rev=num%10
    while i<=rev:
        fact=fact*i
        i=i+1
    count=count+fact
    num=num//10
if count==temp:
    print("Yes")
else:
    print("No")