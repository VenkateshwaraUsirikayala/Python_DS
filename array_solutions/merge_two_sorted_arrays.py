l1=[ 1, 3, 4, 5]
l2=[2, 4, 6, 8]
def merge(arr1,arr2):
    len1=len(arr1)
    len2=len(arr2)
    arr3=[]
    i=j=k=0
    while i<len1 and j<len2:
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    
    while i<len1:
        arr3.append(arr1[i])
        i+=1
    while j<len2:
        arr3.append(arr2[j])
        j+=1
    return arr3

print(merge(l1, l2))