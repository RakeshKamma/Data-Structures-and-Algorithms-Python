
#time complexity- o(2^n)
#space complexity- o(n)

def fib(sample):
    if sample <=2:
        return 1
    else:
        return fib(sample-1)+fib(sample-2)
    

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(45))                                                                                                     