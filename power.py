# Finding the power of the given number

def powernum(num,pow):
    if pow==0:
        return 1
    return num*powernum(num,(pow-1))

print(powernum(3,2))