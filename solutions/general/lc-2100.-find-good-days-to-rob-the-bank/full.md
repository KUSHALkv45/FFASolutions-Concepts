# LC-2100. Find Good Days to Rob the Bank

## 💡 Idea

```
1. This is the first solution - 14-02-26
2 . Idea is just marking 2 indices and between these two the nature of the seq must be dec to inc
3 . more like brute force approach and then bw these two left and right we check if there are indices which satisfy our condition and return 
4 . code also needs improvement as of now



```

## 💻 Code

```python
# 14-02-26
def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        N = len(security)
        if time == 0:
            return [_ for _ in range(N)]

        ans = set()

        if N == 1  :
            if time > 1:
                return list(ans)
            else :
                ans.add(0)
                return list(ans)
       
        i = N-1
        while i > 0:
            if i > 0 and  security[i] < security[i-1] :
                i -= 1

            else:
                j = i
                while j > 0 and security[j] >= security[j-1]:
                    j -= 1
                k = j
                first = -1
                while k > 0 and security[k] <= security[k-1]:
                    if security[k] == security[k-1] and first == -1:
                        first = k
                    k -= 1

                left = k
                right = i

                for z in range(left, right+1):
                    if z-left >= time and right-z >= time and security[z-1] >= security[z] and security[z] <= security[z+1]:
                        ans.add(z)           
                i = k
                if first != -1 :
                    i = first

        if len(ans) == 0:
            return []
        return list(ans)
```

