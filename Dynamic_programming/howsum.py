#m=sum
#n= length of array


#time complexity- o(n*m)
#space complexity- o(m)

def howsum(sum,numbers,memo={}):
    if sum in memo: return memo[sum]
    if sum ==0: return []
    if sum<0: return 0

    for i in numbers:
        remainder= sum - i
        finalresult = howsum(remainder,numbers,memo)
        if finalresult!=0:
            finalresult.append(i)
            memo[sum]= finalresult # Append the value to the list directly
            return memo[sum]  # Return the list

    memo[sum] =0
    return 0

print(howsum(300,[7,14]))