class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        memo = [[-10**6 for _ in range(n1)] for _ in range(n2)]

        # ans = -10**6

        for j in range(n2):
            for i in range(n1):
               
                pro = nums1[i]*nums2[j]
                memo[j][i] = max(memo[j][i] , pro) # nor comp

                # compare with top and left
                if j-1 >= 0 :
                    memo[j][i] = max(memo[j][i],memo[j-1][i]) 
                if i-1 >= 0:
                    memo[j][i] = max(memo[j][i],memo[j][i-1])
                
                # compare with diagonal 
                if j-1 >= 0 and i-1 >= 0 :
                    memo[j][i] = max(memo[j][i],memo[j-1][i-1] + pro)

        return memo[n2-1][n1-1] 