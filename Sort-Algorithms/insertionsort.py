# Complexity - O(n^2)
# Take every element and put it the correct position of left sorted array

def insertionSort(array) -> list:
	arraySize = len(array)
	for index in range(2,arraySize): # First element is already sorted
		prevIndex = index - 1 # Sorting from last element till 0
		while prevIndex > 0 and array[prevIndex] >= array[prevIndex+1]:
			array[prevIndex+1],array[prevIndex] = array[prevIndex],array[prevIndex+1]
			prevIndex = prevIndex - 1
	return array
	
array = [3,66,32,45,98,33,35,359,10]		
print( insertionSort(array) )