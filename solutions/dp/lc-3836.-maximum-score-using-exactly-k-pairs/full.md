# LC-3836. Maximum Score Using Exactly K Pairs

## 💡 Idea

```
-This is same as LC-1458 (https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/)

- Add a additional dimension of k here
- Base for this problem is Knapsack pick/no Pick Tabularization

ex : nums1 : 1,3,2    , nums2 : 4,5,1  k = 2

	x	          4	           5	            1
x	0,0,0	0,0,0	0,0,0	0,0,0
1	0,0,0	0,4,0	0,5,0	0,5,0
3	0,0,0	0,12,0	0,15,19	0,15,19
2	0,0,0	0,12,0	0,15,22	0,15,22

```

## 💻 Code

```python
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N,M = len(nums1),len(nums2)
        neg = -1*(10**14)
        dp = [ [[neg for _ in range(k+1)] for _ in range(M+1) ] for _ in range(N+1) ]

        #base case k = 0
        for i in range(N+1):
            for j in range(M+1):
                dp[i][j][0] = 0

        for i in range(N):
            for j in range(M):
                p = nums1[i]*nums2[j]
                for z in range(1,k+1):
                    dp[i+1][j+1][z] = max(dp[i][j][z-1] + p , dp[i][j+1][z] , dp[i+1][j][z])
        
        return dp[N][M][k]
```

