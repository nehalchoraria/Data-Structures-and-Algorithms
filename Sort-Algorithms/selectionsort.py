# Notes 
# Move from left to right and keeping replacing the smallest element with index
# Complexity - O(n^2)

def selectionSort(array):
	for index in array:
		minValue = index
		for ahead in range(index,len(array)):
			if array[ahead] < array[minValue]:
				minValue = ahead	
		array[minValue],array[index] = array[index],array[minValue]
	return array

unsortedList = [20,5,6,1,44,23,67,89,44,54,7]
selectionSort(unsortedList)