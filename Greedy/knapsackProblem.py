
def buildKnapsack(array,availableWeight):

    profitWeightRatio = [ (index, item[0]/item[1]) for index,item in enumerate(array) ] 
    profitWeightSortedIndex = [ item[0] for item in sorted(profitWeightRatio, key=lambda x: x[1],reverse=True) ]
    profitEarned = 0
    index = 0

    for index in profitWeightSortedIndex:
        if availableWeight > 0 and array[index][1] <= availableWeight:
            profitEarned = profitEarned + array[index][0]
            availableWeight = availableWeight - array[index][1]
        else:
            break
 
    if availableWeight > 0:  #fractional part
        profitEarned = profitEarned + ( array[index][0] * availableWeight ) /array[index][1]
    return format(profitEarned)

# No of objects = N = 7
knapsack = [[10,2],[5,3],[15,5],[7,7],[6,1],[18,4],[3,1]] # [Profit,Weight]

availableWeight = 15
profit = buildKnapsack(knapsack,availableWeight)
print(profit)