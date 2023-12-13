#m=target sum
#n= length of array


#time complexity- o(n*m)
#space complexity- o(m)

def canconstruct_tab(targetstring,substrings):
    table = [False]*(len(targetstring)+1)
    table[0]=True
    for i in range(len(targetstring)):
        if table[i]==True:
            for j in substrings:
                #if j.startswith(targetstring[i]): mistake
                if targetstring[i:i + len(j)] == j:    
                    if (i+len(j))<len(targetstring)+1:
                        table[i+len(j)] = True
            #print(table)

    return table[len(targetstring)]

print(canconstruct_tab('abcdef',['ab','abc','cd','def','abcd']))#true
print(canconstruct_tab('skateboard',['bo','rd','ate','t','ska','sk','boar']))#false
print(canconstruct_tab('enterapotentpot',['a','p','ent','enter','ot','o','t']))#true
print(canconstruct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeet',['e','ee','eee','eeeee','eeeeeee','eeeeeeeeeeeeeeeeeee']))#false
print(canconstruct_tab('',['cat','dog']))#true