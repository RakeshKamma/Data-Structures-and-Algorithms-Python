
#m=target sum
#n= length of array


#time complexity- o(n*m^2)
#space complexity- o(m^2)


def canconstruct(targetstring, substrings,memo={}):
    if targetstring in memo: return memo[targetstring]
    if targetstring == "":
        return 1

    count = 0

    for i in substrings:
        if targetstring.startswith(i):
            remaining_string = targetstring[len(i):]  
            count += canconstruct(remaining_string, substrings)

    memo[targetstring]= count
    return count

# Test cases
print(canconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canconstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canconstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeeeeeeeeeeeeeee']))
print(canconstruct('', ['cat', 'dog']))