arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1] 


def fix(arr):
    s = set()
    n = len(arr)
    for i in range(n):
        s.add(arr[i])
    for i in range(n):
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1


fix(arr)
print(arr)
