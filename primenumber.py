# checkin the number is prome or not

def primenumber(num):

    flag = 0

    for i in range(2,num):
        if num%i==0:
            flag=1
            break
        if flag==1:
            print("prime number")
        else:
            print("Not Prime")

print(primenumber(15))