class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        if(str1==str2):
            return 1
        elif(str1[2:]+str1[0]+str1[1]==str2):
            return 1
        elif(str1[-2]+str1[-1]+str1[:len(str1)-2]==str2):
            return 1
        else:
            return 0