
#m= target string
#n= length of array

#time complexity- o(n^m)
#space complexity- o(m)


def allconstruct(finalstring,substrings):
    #base case
    if finalstring=="": return [[]]

    finallist=[]

    #iterations
    for i in substrings:
        if finalstring.startswith(i):
           temp1list=allconstruct(finalstring[len(i):],substrings)
           temp2list = list(map(lambda x: [i] + x, temp1list))
           finallist.extend(temp2list)
           
    return finallist      



#print(allconstruct('purple',['purp','p','ur','le','purpl']))
print(allconstruct('abcdef',['ab','abc','cd','def','abcd','ef','c']))


     