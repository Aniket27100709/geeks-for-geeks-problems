class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum1=(n*(n+1))//2
        sum2=0
        for i in range(len(array)):
            sum2+=array[i]
        return sum1-sum2