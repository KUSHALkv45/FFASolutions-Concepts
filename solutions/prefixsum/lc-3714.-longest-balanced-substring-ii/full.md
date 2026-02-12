# LC-3714. Longest Balanced Substring II

## 💡 Idea

```
- This goes from prefix sum principal logic:
- if we are finding subarray with sum = req : we use this prefix sum concept :this is the core

- Here only 'a','b','c' chars are present in the string : 
- so only 1 char subtrings ,2 char substrings and 3 char substrings are possible

#Notations : 
# a - char 'a' - count , b- 'b' count and c - 'c' count
# 1 char substring means aaaa or bbbb or cccccc only with one of the char
# 2 char -> aabb , aaccccaa , bc
# 3 char -> abcabc, aabbcc

- For 1 char 
- it is straight forward u keep track of prev char and inc the len till u dont find a new char then u reset 

- For 2 char substrings 
- Consider we have a,b,c as counts  at current index  we are trying for ab substring(2char)
- 1st condition -we need to find index where it has same c val ,so that then the remaining substring will be only with 'a','b'  
- 2nd condition - if  Ax,Bx are a,b val at index x then  a-Ax = b-Bx
- From a-Ax = b-Bx  =>  a-b = Ax-Bx 
- if  at curr index i we have a,b,c  (counts)  if at index x  Ax,Bx,Cx we want Cx = c , a-b = Ax-Bx

- For 3 char substrings   a -Ax  = b-Bx = c-Cx        
- so at index i a,b,c and index x Ax,Bx,Cx  then a-b = Ax-Bx and a-c = Ax-Cx and b-c = Bx-Cx if we find the first 2 then the last cond will pass
- so we find for (a-b),(a-c) and check if there is index with same diff Ax-Bx , Ax-Cx
```

## ⏱️ Time & Space Complexity

TC : O(N) 
SC : O(N)

## 💻 Code

```python
def longestBalanced(self, s: str) -> int:
        a = b = c = 0
        ans = 0
        
        # single letter runs
        last = ''
        run = 0
        
        # for a,b only → (c, a-b)
        ab = {(0, 0): -1}
        
        # for a,c only → (b, a-c)
        ac = {(0, 0): -1}
        
        # for b,c only → (a, b-c)
        bc = {(0, 0): -1}
        
        # for a,b,c → (a-b, a-c)
        abc = {(0, 0): -1}
        
        for i, ch in enumerate(s):
            
            # ---- single letter case ----
            if ch == last:
                run += 1
            else:
                run = 1
                last = ch
            ans = max(ans, run)
            
            # ---- update prefix counts ----
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            
            # ---- a,b only ----
            key = (c, a - b)
            if key in ab:
                ans = max(ans, i - ab[key])
            else:
                ab[key] = i
            
            # ---- a,c only ----
            key = (b, a - c)
            if key in ac:
                ans = max(ans, i - ac[key])
            else:
                ac[key] = i
            
            # ---- b,c only ----
            key = (a, b - c)
            if key in bc:
                ans = max(ans, i - bc[key])
            else:
                bc[key] = i
            
            # ---- a,b,c ----
            key = (a - b, a - c)
            if key in abc:
                ans = max(ans, i - abc[key])
            else:
                abc[key] = i
        
        return ans
```

