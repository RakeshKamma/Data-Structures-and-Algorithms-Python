sample = [3,7,8,5,4,2,6,1,9]

# n - length of sample
#time complexity - O(n*logn)
#spac ecomlexity - O(n)


def mergesort(sample):
    temp_length = len(sample)
    final_result =[]

    if temp_length ==1:
        return sample
        

    if temp_length %2 ==0:
        left_sample = sample[:(temp_length//2)]
        right_sample = sample[(temp_length//2):]
      

    else:
        left_sample = sample[:((temp_length+1)//2)-1]
        right_sample = sample[((temp_length+1)//2)-1:]
    
    
    left_result = mergesort(left_sample)
    right_result = mergesort(right_sample)

    counta=0
    countb=0

    while(counta<len(left_result) and countb< len(right_result)):
        if left_result[counta]<=right_result[countb]:
            final_result.append(left_result[counta])
            counta+=1 
        else:
            final_result.append(right_result[countb])
            countb+=1 
    
    if counta<len(left_result):
        left_Remaining =left_result[counta:]
        final_result.extend(left_Remaining )
    else:
        right_remaining = right_result[countb:]
        final_result.extend(right_remaining)

    return final_result


print(mergesort(sample))