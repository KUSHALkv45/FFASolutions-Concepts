# LC-1653

## 💡 Idea

at any point just keep all the a's to left and only b's to right

This has been added in prefix sum cat too refer that for prefix sum idea

but here adding a constant space idea

## ⏱️ Time & Space Complexity

TC : O(N) + O(N)
SC : O(1)

## 💻 Code

```python
def minimumDeletions(self, s: str) -> int:
        
        # st = []
        n = len(s)
        
        b_left,a_right = 0,s.count('a')

        ans = a_right

        for i in range(n):
            if s[i] == 'a':
                a_right -=1
            else:
                b_left += 1
            ans = min(ans,b_left+a_right)

        return ans
```

