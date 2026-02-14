# LC-1458. Max Dot Product of Two Subsequences

## 💡 Idea

This is a pick/no Pick knapsack problem we use tabulation like this
for example   nums1 = [2,1,-2,5], nums2 = [3,0,-6]
1. We have a order defined here we have to pick elements in order 
2. pick n1-0 , n2 - 2   then we can't pick n2-1 or 0 after this operation - this cond makes this a dp problem
	X	3	0	-6
X	0	0	0	0
2	0	6	0	-12
1	0	6	6	6
-2	0	-6	6	18
5	0	15	6	18

the max dot product possible is 18

## 🔍 Simple Algorithm Trace

make tabulation 
compare with top , left and diagonals and store the max values

## ⏱️ Time & Space Complexity

```
N,M - lengths of arrays num1,nums2
O(N*M) 
```

## 💻 Code

```python
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
```

