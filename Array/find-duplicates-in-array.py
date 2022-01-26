def duplicates(self, arr, n):
        ans = []
        arr2 = [None] * n
        for i in range(n):
             arr2[i] = 0

        for i in range(n):
             arr2[arr[i]] += 1

        for i in range(n):
            if arr2[i] > 1:
                ans.append(i)

        if len(ans):
            return ans
        else:
            return [-1]