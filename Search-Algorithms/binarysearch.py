def binarysearch(arr,target):
    leftIndex = 0
    rightIndex = len(arr) - 1
    while leftIndex <= rightIndex:
        mid = leftIndex + (rightIndex - leftIndex)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            rightIndex = mid - 1
        else:
            leftIndex = mid + 1
            
    return -1

array = [4,5,7,8,10,11,22,43,44,46,78,100,101,102,111,122,123]
target = 44

print(binarysearch(array,target))
            
