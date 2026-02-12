# Lc    3834 Merge Adjacent Equal Elements

## 💡 Idea

use stack principal

## 🔍 Simple Algorithm Trace

```
while st[top] == ourNumber:
             ourNumber += st[top]
              top -= 1
 top += 1
st[top] = ourNumber(finalNumber)

```

## ⏱️ Time & Space Complexity

O(N)

## 💻 Code

```python
top = 0
        for i in range(1,len(nums)):
            j = nums[i]
            while top >= 0 and j == nums[top]:
                j += nums[top]
                top -=1 
            top += 1
            nums[top] = j

        return nums[0:top+1]
```

