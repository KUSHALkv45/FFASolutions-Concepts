
    def minFlipsMonoIncr(self, s: str) -> int:
        c_0 = s.count('0')
        c_1 = 0
        ans = c_0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                c_1 += 1
            else:
                c_0 -= 1
            
            ans = min(ans,c_1 + c_0)
            # i = 4 if s = 0010100 - to make it  0000011  c_1 before i and c_0 after i 
        
        return ans



