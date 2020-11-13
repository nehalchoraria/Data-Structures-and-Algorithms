
# Assuming Left heap and right heap being in order build max heap on index
def maxHeapify(array,index):
    leftIndex = 2*index
    rightIndex = 2*index + 1
    largest = index

    if leftIndex < len(array) and array[leftIndex] > array[index]:
        largest = leftIndex
    if rightIndex < len(array) and array[rightIndex] > array[index]:
        largest = rightIndex
    if largest != index:
        array[largest],array[index] = array[index],array[largest]
        maxHeapify(array,largest)

# Starting from leaf nodes to root node start heapify iteratively
def buildHeap(array):   
    for i in range(len(array)//2 - 1, -1, -1): 
        maxHeapify(array,  i) 
    return array

# Makes last child as parent and calls heapify to top which fixes up tree down the path
def deleteMax(array) -> bool:
    if len(array) < 1:
        return False
    array[0] = array.pop()
    maxHeapify(array,0)
    return True

# Delete first element and re-structure heap. Keep doing this until only 1 element.
def heapSort(array):
    array = buildHeap(array)
    
    sortedList = []
    for _ in range(len(array),1,-1):
        sortedList.append(array[0])
        deleteMax(array)
    sortedList.append(array[0])
    return sortedList

array = [12, 11, 13, 5, 6, 7]
heap = buildHeap(array)
print(heapSort(array))