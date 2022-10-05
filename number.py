

a = [1, 2, 3, 4, 5, 6]
k = 5

import math
def findNumber(arr, k):
    
    arr.sort()
    x = 0
    y = len(arr) - 1
    new = []
    
    while (x <= y):
        
        mid = math.floor((x + y) / 2)
        if arr[mid] == k:
            return "YES"
        elif arr[mid] > k:
            y = mid - 1
            new = arr[:y]
            findNumber(new, k)
        elif arr[mid] < k:
            x = mid
            new = arr[x:]
            findNumber(new, k)
            
    return "NO"


    # if k in arr:
    #     return "YES"
    # else:
    #     return "NO"


print(findNumber(a, k))