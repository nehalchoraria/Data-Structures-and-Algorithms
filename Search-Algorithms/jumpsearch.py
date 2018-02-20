def linearsearch(arr,jumpsize,findelement,startpoint,iterations):
	for i in range(startpoint,startpoint+jumpsize-1):
		iterations = iterations + 1
		if arr[i] == findelement:
			return  "Element found after "+str(iterations)+" iterations at position "+str(i+1)
		else:
			pass
	return "Element not found"
	
def jumsearch(arr,jumpsize,findelement):
	iterations = 0
	check = False
	for i in range(0,len(arr),jumpsize):
		iterations = iterations + 1
		if findelement == arr[i]:
			print("Element found after",iterations,"iterations at position ",i+1)
			check = True
			break
		if findelement > arr[i]:
			pass
		else: 
			print(linearsearch(arr,jumpsize,findelement,i-jumpsize+1,iterations))
			check = True

	if check==False:
		print(linearsearch(arr,jumpsize,findelement,i+1,iterations))

arr = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 57, 89, 144, 233, 377, 610)
jumsearch(arr,4,89)