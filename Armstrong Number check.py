num = int(input("Enter any number:"))
temp = num
count = 0
x = num
n = 0
while x > 0:
    p = x % 10
    n = n + 1
    x = x // 10
print("Number of digits in entered number:", n)
while temp > 0:
    dig = temp % 10
    count = count + dig ** n
    temp = temp // 10
if num == count:
    print("Entered number is an armstrong number.")
else:
    print("Entered number is not an armstrong number.")
