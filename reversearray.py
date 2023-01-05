# Reversing the array

def reversalList(A,s,e):
    A[s],A[e] = A[e],A[s]
    s+=1
    e-=1

A = [10,20,30,40,50]
reversalList(A,2,4)
print(A)