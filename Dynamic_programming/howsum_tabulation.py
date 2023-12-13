#m= target string
#n= length of array

#time complexity- o(n*m^2)
#space complexity- o(m^2)

def howsum_tab(targetsum,numbers):
    table = [None]*(targetsum+1)
    table[0]=[]

    for i in range(targetsum+1):
        if table[i]!=None:
            for j in numbers:
                if i+j<targetsum+1:
                    sample=list(table[i])
                    sample.append(j)
                    table[i+j]= sample


    return table[targetsum]

print(howsum_tab(7,[2,3]))
print(howsum_tab(7,[5,3,4,7]))
print(howsum_tab(7,[2,4]))
print(howsum_tab(8,[2,3,5]))
print(howsum_tab(300,[7,14]))