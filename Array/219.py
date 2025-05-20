#判断一个数组中是否有一个duplciate然后duplicate的index 满足abs(i - j) <= k的条件
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        使用滑动窗口,题目abs(i - j) <= k中的条件是窗口大小.然后我们需要有一个set来记录窗口中的所有元素,每一次移动右指针我们判断当前右指针的元素是否在set里面,在的话就
        return ture,不再的话就继续循环.当窗口的大小超过了abs(i - j) <= k条件,我们就需要移动左指针,这时我们需要把左指针的元素从set中移除
        
        """
        # #method 1 for loop, we increae the j after the second if condition, so we need to use if abs(i-j) >=k
        unique = set()
        l =0
        for r in range(0,len(nums)):
            if nums[r] in unique:
                print(nums[r],r,l)
                return True
            unique.add(nums[r])
            if abs(l-r) >=k:
                unique.remove(nums[l])
                l+=1
        return False
        #method 2 while loop, we increae the j before the second if condition, so we only need to use if abs(i-j) >k
        # i,j = 0,0
        # unique = set()
        # while j < len(nums):
        #     if nums[j] in unique:
        #         return True
        #     unique.add(nums[j])
        #     j = j+1
        #     if abs(i-j) >k:
        #         unique.remove(nums[i])
        #         i+=1
        # return False