n=int(input("Enter number of rows:"))
for i in range(1,(n+1)):
    for j in range(1,(2*n+1)):
        if 1<=(j-i)<=2 and i<=j: 
           print('*\t',end='')
        
        else:
            print(' \t',end='')
    print()