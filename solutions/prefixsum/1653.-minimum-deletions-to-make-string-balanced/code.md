
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
            



