# LC-1 TwoSum

## 💡 Idea

use HashMap  and two pointers with sorting

## ⏱️ Time & Space Complexity

O(N) - hashMap 
two pointers - > O(NlogN)

## 💻 Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map = {}
       for i in range(len(nums)):
        if target-nums[i] in map :
            return [i,map[target-nums[i]]]
        else :
            map[nums[i]] = i
       return []
```

