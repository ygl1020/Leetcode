#计算连续子序列的最大乘积
def maxProduct(self, nums: List[int]) -> int:
        """
        我们持续不断的继续再index i时连续的最大product和最小product,然后遍历整个数组不断更新这两个值,这个过程中不断更新res来获取最后的结果.
        """
        res = max(nums)
        curMax, curMin = 1,1
        for i in nums:
            if i == 0:
                curMax,curMin = 1,1
                continue
            tmp = curMax * i
            curMax = max(curMax*i, curMin*i,i)
            curMin = min(tmp,curMin *i, i)
            print(curMax,curMin)
            res = max(curMax,curMin,res)
        return res