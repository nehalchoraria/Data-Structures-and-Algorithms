# Notes 
# Move from left to right and keeping replacing the smallest element with index
# Complexity - O(n^2)

def selectionSort(inputList):
	for index,element in enumerate(inputList):
		minValue = index
		for ahead in range(index,len(inputList)):
			if inputList[ahead] < inputList[minValue]:
				minValue = ahead	
		inputList[minValue],inputList[index] = inputList[index],inputList[minValue]
	return inputList

unsortedList = [20,5,6,1,44,23,67,89,44,54,7]
selectionSort(unsortedList)