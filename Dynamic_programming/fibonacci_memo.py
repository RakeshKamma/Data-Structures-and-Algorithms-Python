
#memoization-mem


#time complexity- o(n)
#space complexity- o(n)

def fib(sample,mem={}):
    if sample in mem: return mem[sample]
    if sample <=2:
        return 1
    else:
        mem[sample]=fib(sample-1,mem)+fib(sample-2,mem)
        return mem[sample]
    

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(45))                                                                                                     