# Sum of the N natural number in the given number

def sumofnum(num):
    sum = 0 
    for i in range(num+1):
        sum+=i
    return sum

print(sumofnum(8))