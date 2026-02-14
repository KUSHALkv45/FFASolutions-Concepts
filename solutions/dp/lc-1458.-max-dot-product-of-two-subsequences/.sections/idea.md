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
