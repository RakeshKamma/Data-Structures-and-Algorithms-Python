#m=target sum
#n= length of array


#time complexity- o(m^2*n)
#space complexity- o(m)

def canconstruct_tab(targetstring,substrings):
    table = [0]*(len(targetstring)+1)
    table[0]=1
    for i in range(len(targetstring)):
        if table[i]!=0:
            for j in substrings:
                if targetstring[i:i + len(j)] == j:    
                    if (i+len(j))<len(targetstring)+1:
                        table[i+len(j)] +=table[i]
            #print(table)

    return table[len(targetstring)]

print(canconstruct_tab('purple',['purp','p','ur','le','purpl']))
print(canconstruct_tab('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct_tab('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canconstruct_tab('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(canconstruct_tab('',['cat','dog']))