x=input("Enter a string:")
y=x[0]
z=x[-1]
print("First character of a string:",y)
print("Last character of a string:",z)
swap=z+x[1:-1]+y
print(swap)
