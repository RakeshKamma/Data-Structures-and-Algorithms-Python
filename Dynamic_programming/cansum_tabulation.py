#m=target sum
#n= length of array


#time complexity- o(m*n)
#space complexity- o(m)


def cansum_tab(targetsum,numbers):
    table=[False]*(targetsum+1)
    table[0]=True
    for i in range(targetsum+1):
        if table[i]==True:
            for j in numbers:
                if i+j<(targetsum+1):
                    table[i+j] = True


    return table[targetsum] 


print(cansum_tab(7,[2,3]))
print(cansum_tab(7,[5,3,4,7]))
print(cansum_tab(7,[2,4]))
print(cansum_tab(8,[2,3,5]))
print(cansum_tab(300,[7,14]))