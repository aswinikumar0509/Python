# Finding the number of the factor in the given number

def factor(num):
    result = []
    for i in range(1,num+1):
        if num%i==0:
            result.append(i)
    return result

print(factor(10))
