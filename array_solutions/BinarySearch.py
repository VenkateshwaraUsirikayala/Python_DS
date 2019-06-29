def binarySearch(arr, e):
    l=0
    n=len(arr)
    r=n-1
    while l<r:
        mid = int((l+r)/2)
        if arr[mid]==e:
            print('element found at', mid)
            return
        elif e>arr[mid]:
            l=mid+1
        elif e<arr[mid]:
            r=mid-1
    return "element not found"

binarySearch([4,8,9,55,65,99], 65)