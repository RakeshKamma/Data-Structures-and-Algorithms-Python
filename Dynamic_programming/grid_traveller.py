#time complexity- o(m*n)
#space complexity- o(m+n)


def gridtraveller(m,n,mem={}):
    if (m,n) in mem: return mem[(m,n)]
    if m==0 or n==0: return 0
    if m==1 and n==1: return 1
    else:
        mem[(n,m)]=mem[(m,n)]=gridtraveller(m-1,n,mem)+gridtraveller(m,n-1,mem)
        return mem[(m,n)]


print(gridtraveller(18,18))