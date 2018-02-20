def binarysearch(arr,value):
    mid = (int)(len(arr)/2)
    iters = 1
    left = 0
    right = len(arr) - 1
    last = -1
    
    while(left<right and last!=mid):
        last = mid
        if arr[mid] == value:
            print("Found in",iters,"iterations")
            return "Location : "+str(mid+1)
        elif  arr[mid] > value:
            right = mid
            mid = (int)( (left + right) /2)
        elif arr[mid] < value:
            left = mid
            mid = (int)(  (left + right) /2 )
        iters = iters + 1
    return "Not found"

print(binarysearch([4,5,7,8,10,11,22,43,44,46,78,100,101,101,102,111,111,122,122,123],100))
            
