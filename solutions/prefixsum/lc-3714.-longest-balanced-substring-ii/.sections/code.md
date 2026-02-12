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