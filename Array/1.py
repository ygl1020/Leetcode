#给你一个数组,让你找到两个元素相加和为target的index
def twoSum(self, nums, target):
        # brute force
        # for i in range(1,len(nums)):
        #     for j in range(0,i):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # method2
        """
        创建一个字典用来存储遇见过的value,然后只需要一个for循环,循环里面我们计算当前element和target的差,然后找字典里面是否有这个元素,有的话我们直接返回,否者
        的话就把当前元素放入字典中.最后如果循环结束还是没有发现满足条件的组合就返回空的数组
        """
        seen = {}
        for i,v in enumerate(nums):
            diff = target-v
            if diff in seen:
                return [i,seen[diff]]
            seen[v] =i
        return [] 
    
