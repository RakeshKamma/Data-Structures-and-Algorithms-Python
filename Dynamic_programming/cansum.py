
#m=targetsum
#n= length of array

#time complexity- o(n*m)
#space complexity- o(m)

def cansum(targetsum,numbers,memo={}):
    if targetsum in memo: return memo[targetsum]
    if targetsum==0: return True
    if targetsum<0: return False

    for i in numbers:
        remainder = targetsum -i
        memo[targetsum]=cansum(remainder,numbers,memo) 
        if memo[targetsum]==True:
            return True

    return False

print(cansum(400,[14,17]))