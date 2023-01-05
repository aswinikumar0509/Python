# python program to count the unique element

def count(arr,n):

    # Make all the array element not visited
    visisted = [False for i in range(n)]
    count_dis = 0
    # Traverse throught the array element
    # Traverse the count frequency

    for i in range(n):
        # Skip the element already visisted
        if(visisted[i]==True):
            continue
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visisted[j]=True
        count_dis+=1

    print(count_dis)

arr = [10,30,40,20,10,20,50,10]
n = len(arr)
count(arr,n)