#给你一个unsorted数组,让你在o(n)时间内找到最长连续的子序列长度
def longestConsecutive(self, nums: List[int]) -> int:
        """
        我们需要先找到每一个sequence的开始点,如何确认这个开始点可以再set(nums)里面查看是否存在(i-1), 如果存在我们就进入while循环记录当前sequence的长度.一直到结束然后更新res的大小
        """
        unique = set(nums)
        res =0
        for i in unique: # error for checking nums # 注意这里我们直接用unique就好了, 不需要用nums
            if (i-1) not in unique:
                long = 0
                while (i+long) in unique:
                    long +=1
                res = max(long,res)
        return res
