
#       weight -         |  0  | 1 | 2 | ..............  9
#       ---------------------------------------------------
#       arraySize  -  0  | 00 | 01 |02 | ..............  09
#                     1  | 10 | 11 |12 | ..............  19
#                     .  | .   .   .             .
#                     .  | .   .   .             .
#                     .  | .   .   .             .
#       arraySize     5  | 50 | 51 |52 | ..............  59

#dp - bottomUp
def subsetSum(array,size):
    dp = [  [False for _ in range(size+1)] for _ in range(len(array)+1)  ]  
    dp[0][0] = True
    for i in range(len(array)+1):
        dp[i][0] = True
    for i in range(1,len(array)+1):
        for j in range(1,size+1):
            if j < array[i-1]: 
                dp[i][j] = dp[i-1][j] 
            if j>= array[i-1]: 
                dp[i][j] = (dp[i-1][j] or dp[i - 1][j-array[i-1]]) 
    return dp[-1][-1]
    
#recursive
def subsetSumRecursive(array,size):
    if size == 0:
        return True
    if len(array) == 0:
        return False 
    elif size < array[0]:
        return subsetSum(array[1:],size)
    else:
        return subsetSum(array[1:],size-array[0]) or subsetSum(array[1:],size)

array = [6,3,2,1]
weight = 5

result = subsetSum( array, weight )
print(result)