#1
"""
这题是求当前数组中是否有两个index的value相加可以等于target,解题思路暴力解法是用两个for循环

为什么会想到用哈希表:最优解是遍历创建一个dict,这个dict会放我们遍历过的所以元素,dict的key是element的value,value是element的index.在遍历数组中我们每一次只要确认targe-i的值是否在dict里面就知道找到元素了没有
                    因为dict的查询只需要o(1)的时间所以总时间只需要o(1)
哈希表为什么用map: map储存的是key和value 用set只可以储存一个合集所以index就储存不了了
本题map是用来存什么的 : 遍历过的element
map中的key和value用来存什么的: key是element的值vlaue是index
"""
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # #method 1
        # res = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i !=j:
        #             res.append(i)
        #             res.append(j)
        #             return res
        # method 2
        seen = {}
        for i,v in enumerate(nums):
            print(i,v)
            rest = target - v
            if rest in seen:
                return [seen[rest],i]
            seen[v] = i
        return []
