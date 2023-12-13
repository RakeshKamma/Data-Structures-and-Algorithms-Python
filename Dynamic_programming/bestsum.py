


#m=target sum
#n= length of array


#time complexity- o(n*m)
#space complexity- o(m)

def bestsum(targetsum,numbers,memo={}):

    #base conditions
    if targetsum in memo: return memo[targetsum]
    if targetsum ==0: return []
    if targetsum<0: return None

    #Store optimized list
    optimal = None

    #iteration
    for i in numbers:
        remainder = targetsum-i
        result = bestsum(remainder,numbers,memo)
        if result != None: 
                result.append(i)
                if (optimal==None or len(result)<len(optimal)):
                    optimal=result
                    

    #implement memoization
    memo[targetsum]= optimal
    return optimal



print(bestsum(7,[5,3,4,7]))
print(bestsum(8,[2,3,5]))
print(bestsum(8,[1,4,5]))
