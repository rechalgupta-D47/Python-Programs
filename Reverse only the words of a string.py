# Reverse only the words of a string
a="The Angaar Batch"
l=a.split()
ans=''
for i in l:
    ans=ans+i[::-1]
    ans=ans+' '
print(ans)


