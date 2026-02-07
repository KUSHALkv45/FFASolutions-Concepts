# 1653. Minimum Deletions To Make String Balanced

## 💡 Idea

Idea is brute force like :

starting from 0 to n(len of string), consider each index as a pivot

before pivot only a's are allowed and from pivot only b'a are allowed

ex: if 2 is the pivot :   aabbbbb        

Use prefix sum and store a counts and b counts

## ⏱️ Time & Space Complexity

TC : O(N) - for prefix and O(N) for pivot traverse
SC : O(N) - for prefix sums

## 💻 Code

```python
def minimumDeletions(self, s: str) -> int:
        
        pref = []

        a,b =0,0
        for c in s:
            if c == 'a':
                a += 1
            else:
                b += 1
            pref.append([a,b])
        

        ans = min(pref[-1][0],pref[-1][1])  # del all 'a' or 'b'

        for i in range(len(s)):
            # if pivot at i means before i all 'a' and rest all 'b'

            # del all 'b' before i and 'a' >= i

            bcount = 0
            acount = pref[-1][0]
            if i > 0:
                bcount = pref[i-1][1]
                acount -= pref[i-1][0]
            
            ans = min(ans,acount + bcount)
        
        return ans
```

