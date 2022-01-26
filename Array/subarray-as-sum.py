class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        start=0
        subarray=0
        if n<=0:
            return [-1]
        for i in range(n):
            subarray+=arr[i]
            while (subarray>s):
                subarray-=arr[start]
                start+=1
            if subarray==s:
                return [start+1,i+1]
        return [-1]