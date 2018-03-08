def merge(a,b):
    (m,n,c) = (len(a),len(b),[])
    (i,j) = (0,0)
    
    while i+j < m+n:
        if i >= m:
            c.append(b[j])
            j = j+1
        elif j >= n:
            c.append(a[i])
            i = i + 1
        elif a[i] >= b[j]:
            c.append(b[j])
            j = j+ 1
        elif b[j] > a[i]:
            c.append(a[i])
            i = i+1
    
#    print(c)
    return c


def mergesort(a,left,right):
    if right - left <= 1:
        return a[left:right]
    else:
        mid = (left+right)//2
        
        L = mergesort(a,left,mid)
        R = mergesort(a,mid,right)
        return (merge(L,R))
        

x = [10,12,4,1,55,7,24,68,2,46,11,32,19,0,1,232,45]
print ( mergesort(x,0,len(x)) )