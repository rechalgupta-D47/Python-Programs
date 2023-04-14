n=int(input("Enter number of rows:"))
for i in range(1,(n+1)):
    for j in range(1,(2*n+1)):
        if i>=j: 
           print('*\t',end='')
        elif (i+j)>=(2*n+1):
           print("*\t",end='')
        
        else:
            print(' \t',end='')
    print()