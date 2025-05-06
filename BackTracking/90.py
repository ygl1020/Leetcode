#一个带有重复值的数组,找出所有的子集subest
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        这题是纵向可以有重复的,但是横向不可以有重复的. 树层去重的原因是因为当nums进行排序,如果再nums:[1,2,2,3]那么再第一个2我们开始向下递归的时候就已经遍历过了2，2，3的所有的情况,
        那么第二个2开始如果还继续遍历的话就会有重复的值.因此我们进行树层去重.去重的操作是判断i是否i是否大于startindex,并且nums[i-1]==nums[i]
        """
        if not nums:
            return [[]]
        nums.sort()
        res,path,startIndex = [[]],[],0
        def backtraking(nums,startIndex):
            if startIndex>=len(nums):
                return
            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:#树层去重的代码写错了.我之前写的是nums[startIndex] == nums[startIndex].我们树层去重是在当前for循环层进行的,因此是num[i]和nums[i-1].i>startIndex是为了防止出现负数的情况
                    continue
                else:
                    path.append(nums[i])
                    res.append(path[:])
                    backtraking(nums,i+1)
                    path.pop()
        backtraking(nums,startIndex)
        return res