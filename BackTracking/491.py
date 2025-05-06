#给定一个数组,不能给数组排序求递增且长度至少为2的所有子集
def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        这题的难点在于1)如何去重,并且是树层方面横向去重 -->每次新的层级遍历开始时初始化一个空的数组used然后每次判断是否nums[i]再used里面.因为每一层我们都要重置一下used数组
        所以它应该放在for循环的外面 2)如何确保是递增的-->比较nums[i]和path[-1]的值  3)如何确保path的长度至于为2--> 对比len(path)

        """
        if not nums:
            return []
        res,path,startIndex = [],[],0
        def backtracking(nums,startIndex):
            if startIndex >=len(nums):
                return
            used = [] 
            for i in range(startIndex,len(nums)):
                # if i>startIndex and nums[i] ==nums[i-1]:
                #     continue
                if (startIndex>0 and nums[i] <path[-1]) or nums[i] in used:
                    continue 
                used.append(nums[i])
                path.append(nums[i])
                if len(path) >=2:
                    res.append(path[:])
                backtracking(nums,i+1)
                path.pop()

        backtracking(nums,startIndex)
        return res
    
    
        #method 2
        if not nums:
            return [[]]
        path,res,startIndex = [],[],0
        def backtracking(nums,startIndex):
            if startIndex == len(nums):
                return 
            tmp = path
            used = [] # error 1 这里不可以对数组进行排序所以需要一个used数组来更新每一层用过了哪一个node
            for i in range(startIndex,len(nums)):
                if tmp and nums[i]< tmp[-1]:
                    continue  # error 2 这里应该是continue而不是return,否者subtree其他的节点还没有被探索完
                if nums[i] in used:
                    continue
                used.append(nums[i])
                path.append(nums[i])
                if len(path) >=2:
                    res.append(path[:])
                    backtracking(nums,i+1)
                    path.pop()
                else:
                    backtracking(nums,i+1)
                    path.pop()

        backtracking(nums,startIndex)
        return res