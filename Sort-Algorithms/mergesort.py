def mergeList(leftList,rightList):
    leftListLen = len(leftList) 
    rightListLen = len(rightList)
    combinedList = []
    (l,r) = (0,0)

    while ( l < leftListLen and r < rightListLen ):
        if leftList[l] > rightList[r]:
            combinedList.append(rightList[r])
            r += 1
        else:
            combinedList.append(leftList[l])
            l += 1
    
    while( l < leftListLen ):
        combinedList.append(leftList[l])
        l += 1
    
    while ( r < rightListLen ):
        combinedList.append(rightList[r])
        r += 1

    return combinedList

def mergesort(a,left,right):
    if right - left <= 1:  # Split into left and right list continously until size is 1
        return a[left:right]
    else:
        mid = (left+right)//2
        
        L = mergesort(a,left,mid)   
        R = mergesort(a,mid,right)
        a = mergeList(L,R) # Keep Merging left and right list and move up the tree
        return a

x = [1,2,4,6,3,5,7,8]
y = mergesort(x,0,len(x))
print(y)


