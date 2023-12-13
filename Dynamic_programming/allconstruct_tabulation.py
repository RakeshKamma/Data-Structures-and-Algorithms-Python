#m= target string
#n= length of array

#time complexity- o(n^m)
#space complexity- o(n^m)

def allconstruct_tabulation(targetstring, substrings):
    size = len(targetstring)
    table = [[] for _ in range(size + 1)]
    table[0] = [[]]

    for i in range(size):
        if table[i]:
            for j in substrings:
                if targetstring[i:i+len(j)] == j:
                    temp = list(map(lambda x: [j] + x, table[i]))
                    table[i + len(j)].extend(temp)

    return table[size]

# Test case
result = allconstruct_tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])
print(result)
