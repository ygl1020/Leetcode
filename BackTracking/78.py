#再一个数组中找到所有的子集
def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        subset子集问题和组合已经字符串分割不太一样.组合和字符串分割我们是在叶子节点收集结果,但是自己问题的我们是在node节点就开始收集结果了
        因为是在一个数组里收集子集,为了避免出现重复我们需要用startIndex来记录当前的遍历到哪个位置了
        """
        res,path,startIndex = [[]],[],0
        def backtracking(nums,startIndex):
            if startIndex>=len(nums):
                return
            for i in range(startIndex,len(nums)):
                path.append(nums[i])
                res.append(path[:])
                backtracking(nums,i+1)
                path.pop()
        backtracking(nums,startIndex)     
        return res