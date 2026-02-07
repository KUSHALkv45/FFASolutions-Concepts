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