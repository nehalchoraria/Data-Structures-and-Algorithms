
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

def buildHeap(array):   
    for i in range(len(array)//2 - 1, -1, -1): 
        maxHeapify(array,  i) 
    return array

def deleteMax(array) -> bool:
    if len(array) < 1:
        return False
    array[0] = array.pop()
    maxHeapify(array,0)

array = [12, 11, 13, 5, 6, 7]
heap = buildHeap(array)
print(heap)
deleteMax(array)
print(heap)