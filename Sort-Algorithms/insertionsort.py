# Complexity - O(n^2)

def insertionsort(arr):
	for index,value in enumerate(arr):
		j = index - 1
		while ( j > 0 ):
			if arr[j] >= arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
			else:
				break
			j = j - 1
	
	print(arr)
			
insertionsort([3,66,32,45,98,33,35,359,10])