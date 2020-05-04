# Complexity - O(n^2)

def insertionsort(arr):
	for rightindex in range(len(arr)):     #For every element in array
		checkpoint = rightindex       		# keep comparing with previous elements until element behind is 
		while checkpoint>0 and arr[checkpoint] < arr[checkpoint - 1]:	# smaller and keep swapping
			(arr[checkpoint],arr[checkpoint-1]) = (arr[checkpoint-1],arr[checkpoint])
			checkpoint = checkpoint - 1
	print(arr)

insertionsort(list(range(500,0,-1)))