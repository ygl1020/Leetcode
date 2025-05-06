#给你一个重复的数组,求全部的排列可能性
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        两种树层去重的办法,第一种是用used=[false]*len(nums),然后我们用i >0 and nums[i] == nums[i-1] and not used[i - 1],这里需要加not used[i-1]是因为如果是数组1，1，1.当我们遍历完第一个1的全部可能性,我们开始遍历第二个1,这时由于回溯的原因第一个1的used会等于false
        第二种办法的话是通过再for外边放置一个空数组，然后通过判断nums[i]是否再used数组里面来去重.由于每次递归的往下的时候used数组都重置为空因此不需要进行回溯
        """
        #method 1
        if not nums:
            return []
        nums.sort()
        path,res,used = [],[],[False]*len(nums)
        def backtracking(nums):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if (i >0 and nums[i] == nums[i-1] and not used[i - 1]) or used[i]: #used[i-1]代表的是之前的那个重复值已经取完了->eg:1,1,1我么先处理第一层第一个1,之后回溯第一层然后处理第二个1,这个时候used[0]会等于0因为回溯的原因.因此这个条件是必须的
                    continue
                else:
                    used[i] =True
                    path.append(nums[i])
                    backtracking(nums)
                    used[i]=False
                    path.pop()

        backtracking(nums)
        return res
        # method2
        if not nums:
            return []
        nums.sort()
        path,res,used = [],[],[False]*len(nums)
        def backtracking(nums):
            if len(path)==len(nums):
                res.append(path[:])
                return
            tmp = []
            for i in range(len(nums)):
                if nums[i] in tmp or used[i]: #used[i-1]代表的是之前的那个重复值已经取完了->eg:1,1,1我么先处理第一层第一个1,之后回溯第一层然后处理第二个1,这个时候used[0]会等于0因为回溯的原因.因此这个条件是必须的
                    continue  
                tmp.append(nums[i])
                used[i] = True    
                path.append(nums[i])
                backtracking(nums)
                path.pop()
                used[i] = False 
        backtracking(nums)
        return res