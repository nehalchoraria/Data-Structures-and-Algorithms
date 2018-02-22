def selectionsort(arr):
	for i in range(len(arr)):
		smallest_index = i
		for j in range(i,len(arr)):
			if arr[smallest_index] > arr[j]:
				smallest_index = j
		(arr[i],arr[smallest_index]) = (arr[smallest_index],arr[i])
	print(arr)
selectionsort([10,2,15,7,8,43,22,25,66,70,1])