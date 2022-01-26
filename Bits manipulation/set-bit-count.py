def findPower(n):
    x=0
    while ((1<<x)==n):
        x+=1
    return x-1
def main(n):
    if (n<=1):
        return n
    x=findPower(n)
    return (x*pow(2,x-1)+(n-pow(2,x)+1)+main(n,pow(2,x)))
N=15
print(main(15))