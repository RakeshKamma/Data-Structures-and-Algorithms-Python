#m= target string
#n= length of array

#time complexity- o(n^m)
#space complexity- o(n^m)

def howsum_tab(targetsum,numbers):
    table = [None]*(targetsum+1)
    table[0]=[]

    for i in range(targetsum+1):
        if table[i]!=None:
            for j in numbers:
                if i+j<targetsum+1:
                    sample=list(table[i])
                    sample.append(j)
                    if table[i+j] is None or len(table[i+j])> len(sample):
                        table[i+j]= sample


    return table[targetsum]


print(howsum_tab(7,[5,3,4,7]))
print(howsum_tab(8,[2,3,5]))
print(howsum_tab(8,[1,4,5]))
print(howsum_tab(100,[1,2,5,25]))