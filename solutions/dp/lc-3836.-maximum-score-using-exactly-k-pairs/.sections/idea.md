-This is same as LC-1458 (https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/)
```


- Add a additional dimension of k here
- Base for this problem is Knapsack pick/no Pick Tabularization

ex : nums1 : 1,3,2    , nums2 : 4,5,1  k = 2

	x	          4	           5	            1
x	0,0,0	0,0,0	0,0,0	0,0,0
1	0,0,0	0,4,0	0,5,0	0,5,0
3	0,0,0	0,12,0	0,15,19	0,15,19
2	0,0,0	0,12,0	0,15,22	0,15,22

```