# Complexity O(nlogn)

def partitionLogic(array,start,end):
    partitonIndex = start
    for i in range(start,end):
        if array[i] < array[end]: #end is pivot
            array[i],array[partitonIndex] = array[partitonIndex],array[i]
            partitonIndex += 1
    array[partitonIndex],array[end] = array[end],array[partitonIndex]
    return partitonIndex 

def quickSort(array,start,end):
    if start < end:
        pivot = partitionLogic(array,start,end) 
        quickSort(array,start,pivot - 1)
        quickSort(array,pivot + 1,end)

x = [2,1,3,6,8,5,7,4]
quickSort(x,0,7)
print(x)