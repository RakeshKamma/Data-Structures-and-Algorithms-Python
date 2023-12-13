
#m=target string
#n= length of array

#time complexity- o(n*m^2)
#space complexity- o(m^2)



def canconstruct(targetstring,substrings,memo={}):
    if targetstring in memo: return memo[targetstring]
    if targetstring=="": return True
  

    for i in substrings:
        if targetstring.startswith(i):
            memo[targetstring] = canconstruct(targetstring.replace(i,""),substrings)
            if memo[targetstring] == True:
                return True
            
    
    return False

print(canconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canconstruct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeet',['e','ee','eee','eeeee','eeeeeee','eeeeeeeeeeeeeeeeeee']))
print(canconstruct('',['cat','dog']))