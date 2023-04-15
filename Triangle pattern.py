n = int(input("Enter number of rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('* ', end='')
    print()
print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j,'\t', end='')
    print()
print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i,'\t', end='')
    print()
print()

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print('* ', end='')
    print()
print()

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(i,'\t', end='')
    print()
print()

for i in range(n, 0, -1):
    a = 5
    for j in range(1, i + 1):
        print(a,'\t', end='')
        a = a - 1
    print()
print()
