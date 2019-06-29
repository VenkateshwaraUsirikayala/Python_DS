n=255
x=bin(n)
x=x.split('0b')[1]
l=len(x)
list_=[]
for i in range(l):
    if x[i]=='1':
        list_.append('0')
    else:
        list_.append('1')
print("".join(list_))
