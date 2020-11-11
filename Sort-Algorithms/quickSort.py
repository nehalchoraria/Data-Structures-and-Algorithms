# Complexity O(nlogn)

def partitionLogic(array,start,end):
    lowerIndex = start
    for i in range(start,end):
        if array[i] < array[end]: #end is pivot
            array[i],array[lowerIndex] = array[lowerIndex],array[i]
            lowerIndex += 1
    array[lowerIndex],array[end] = array[end],array[lowerIndex] #Last element is set to correct position
    return lowerIndex 

def quickSort(array,start,end):
    if start < end:
        pivot = partitionLogic(array,start,end) 
        quickSort(array,start,pivot - 1)
        quickSort(array,pivot + 1,end)

x = [2,1,3,6,8,5,7,4]
quickSort(x,0,7)
print(x)