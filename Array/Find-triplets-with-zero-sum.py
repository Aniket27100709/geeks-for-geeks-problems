from itertools import combinations
class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        for i in combinations(arr,3):
            if sum(i)==0:
                return True
        return False