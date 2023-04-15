s = (input("Enter a string:"))
c1 = s[0]
print("First character of entered string:", c1)
cl = s[-1]
print("Last character of entered string:", cl)
print("Reverse of entered string:", s[-1::-1])
l = len(s)
lh = int((l-1)/2)
print("Middle character of entered string:", s[lh])