class Solution:
    def majorityElement(self, A, N):
        #Your code here
        majority=-999999
        count=0
        freq=0
        for i in range(0,N):
            if (count==0):
                majority=A[i]
                count=1
            else:
                if(majority==A[i]):
                    count=count+1
                else:
                    count=count-1
        for i in range(0,N):
            if(majority==A[i]):
                freq=freq+1
        if(freq>N/2):
            return majority
        else:
            return -1