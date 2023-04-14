a=0
b=1
c=a+b
n=int(input("Enter number of terms:"))
print("fibonacci series:",end=' ')
print(a,end=',')
print(b,end=',')
for i in range(c,n-1):
    c = a + b
    a = b
    b = c

    print(c,end=',')
    c=c+i