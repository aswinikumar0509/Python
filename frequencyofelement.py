# Finding the frequency of the element in the array
def countfreq(arr,n):

    visited = [False for i in range(n)]

    for i in range(n):

        if (visited[i]==True):
            continue

        count = 1
        for j in range(i+1,n,1):
            if(arr[i]==arr[j]):
                visited[j]==True
                count +=1

        print(arr[i],count)

arr = [10,30,10,20,10,20,30,10]
n = len(arr)
countfreq(arr,n)