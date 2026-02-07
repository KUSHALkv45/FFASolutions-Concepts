class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        ans = n -1

        # Bin search
        # for i in range(n-1,-1,-1):
        #     l,r = 0,i-1
        #     idx = -1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if nums[mid]*k >= nums[i]:
        #             idx = mid
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     if idx != -1:
        #         ans = min(ans,idx + (n-1 -i))

        # 2P

        i ,j = n-1,n-1

        while i<= j :
            while  i >= 0 and nums[i]*k >= nums[j]:
                i -= 1
            ans = min(ans,n - (j-i))
            if i == 0:
                break
            j -= 1
        
        

        
        return ans


