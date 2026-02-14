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