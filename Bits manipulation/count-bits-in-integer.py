# Brian Kernighan’s Algorithm
def countBits(n):
    count=0
    while(n):
        n&=(n-1)
        count+=1
    return count
a=14
print(countBits(a))