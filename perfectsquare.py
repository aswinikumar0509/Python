# Finding the perfect square number
import math
def check_perfectsquare(x):
    if (math.ceil(math.sqrt(x))==math.floor(math.sqrt(x))):
        print("True")
    else:
        print("False")

print(check_perfectsquare(84))