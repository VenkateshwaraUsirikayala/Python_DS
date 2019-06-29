arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 

def rearrange(arr):
    n=len(arr)
    j=-1
    for i in range(n):
        if arr[i]<0:
            j+=1
            arr[i],arr[j]=arr[j],arr[i] 
    
#     pos=j+1
#     neg=0
#     
#     while pos<n and neg<pos:
#         arr[neg],arr[pos]=arr[pos],arr[neg]
#         pos+=1
#         neg+=2
     

rearrange(arr)
print(arr) 