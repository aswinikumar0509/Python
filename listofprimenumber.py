# List the prime number between the two number

def getprime(num1,num2):
    prime = []

    for i in range(num1,num2+1):
        flag = 0
        if i<2:
            continue
        if i==2:
            prime.append(i)
            continue
        for x in range (2,i):
            if i%x==0:
                flag==1
                break
        if flag == 0:
           return prime.append(i)

print(getprime(2,10))
        



        