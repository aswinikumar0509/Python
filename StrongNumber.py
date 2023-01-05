# Finding the strong Number 

def is_strong_number(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    sum_of_factorials = 0
    for digit in str(n):
        sum_of_factorials += factorial(int(digit))

    return sum_of_factorials == n

num=145
if (is_strong_number(num) == num):
    print("Yes",num,"is a strong Number.")
else:
    print("No",num,"is not a strong Number.")
