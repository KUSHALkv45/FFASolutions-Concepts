top = 0
        for i in range(1,len(nums)):
            j = nums[i]
            while top >= 0 and j == nums[top]:
                j += nums[top]
                top -=1 
            top += 1
            nums[top] = j

        return nums[0:top+1] 