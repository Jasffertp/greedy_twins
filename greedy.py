#Author: JASFFER T PADIGDIG
#Date: October 29, 2020
#Description: The code takes in an array and computes the minimum number of values to take to be greater than the remaining array
#the input is an array and the expected output is the least number of values the program needs to take to be greater than the sum of the remaining values
#References: 

def greedy(a):
    alength = len(a)
    total = 0
    prev = 0
    
    for i in range(alength):
        total += a[i]
    
    mid = total//2
    
    #for i in range(alength):
    #    num += a[i]
    #    count += 1
    #    if num > mid:
    #        break
        
    for i in range(alength):
        count = 1
        num = a[i]
        
        for j in range(alength):
            if num > mid:
                break
            
            num += a[j]
            count += 1
            
        if count < prev:
            prev = count
        
    return count

a = [2,1,2,4]
print (f'your array is: {a}')
print('')
print(f'the least amount of values you need to be greater than the remaining values is: {greedy(a)}')