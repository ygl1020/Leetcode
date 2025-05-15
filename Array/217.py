#给你一个数组让你求数组里面是否又重复值
def containsDuplicate(self, nums: List[int]) -> bool:
        #method 1
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        #method2
        unique = {}
        for i in nums:
            if str(i) not in unique:
                unique[str(i)] =1
            else:
                unique[str(i)] +=1
            if unique[str(i)] >=2:
                return True
        return False