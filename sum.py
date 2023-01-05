# Sum of the N number using the formula

def sumNnatural(number):
    sum = 0
    sum = int(number*(number+1)/2)
    return sum

print(sumNnatural(8))