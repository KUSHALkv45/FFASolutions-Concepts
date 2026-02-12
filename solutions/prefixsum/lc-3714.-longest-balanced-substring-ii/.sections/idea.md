```
- This goes from prefix sum principal logic:
- if we are finding subarray with sum = req : we use prefix sum concept this basic is the core

- Here only 'a','b','c' chars are present in the string : 
- so only 1 char subtrings ,2 char substrings and 3 char substrings are possible

#Notations : 
# a - char 'a''s count , b- 'b' count and c - 'c' count
# 1 char substring means aaaa or bbbb or cccccc only with one of the char
# 2 char -> aabb , aaccccaa , bc
# 3 char -> abcabc, aabbcc

- For 1 char 
- it is straight forward u keep track of prev char and inc the len till u dont find a new char then u change it 

- For 2 char substrings 
- Consider we have a,b,c as counts  at current index  we are trying for ab substring(2char)
- first we need to find index where it has same c val ,so that then the remaining substring will be only with 'a','b' 
-if  Ax,Bx are a,b val at index x then  a-Ax = b-Bx
- From a-Ax = b-Bx  =>  a-b = Ax-Bx 
- if  at curr index i we have a,b,c  (counts)  if at index x  Ax,Bx,Cx we want Cx = c , a-b = Ax-Bx

- For 3 char substrings   a -Ax  = b-Bx = c-Cx        
- so at index i a,b,c and index x Ax,Bx,Cx  then a-b = Ax-Bx and a-c = Ax-Cx and b-c = Bx-Cx if we find the first 2 then the last cond will pass
- so we find for (a-b),(a-c) and check if there is index with same diff Ax-Bx , Ax-Cx
```