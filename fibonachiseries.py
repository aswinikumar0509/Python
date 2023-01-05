# Finding the fibnachi sereies if the n th element

def fibonachi(n):
    if n<=1:
        return n
    else:
        return fibonachi(n-1)+fibonachi(n-2)

print(fibonachi(5))