# 寻找下一个permutation
def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force solutuion
        # if not nums:
        #     return []
        # copy = nums[:]
        # nums.sort()
        # path,res,used = [],[],[False]*len(nums)
        
        # def backTracking(nums):
        #     if len(path)==len(nums):
        #         res.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         # if (i>0 and nums[i] == nums[i-1] and not used[i]) or used[i]:
        #         if (i >0 and nums[i] == nums[i-1] and not used[i - 1]) or used[i]:
        #         # if used[i]:
        #             continue
        #         else:
        #             path.append(nums[i])
        #             used[i]=True
        #             backTracking(nums)
        #             path.pop()
        #             used[i]=False
        # backTracking(nums) 
        # idx = res.index(copy)
        # next_perm = res[idx + 1] if idx != len(res) - 1 else res[0]
        # nums[:] = next_perm 
        
        #optimal
        """
        在示例中我们可以发现在数组[1，2,3,2,1]中,下一个permutation不可能在倒数三个index中发生,因为他们是从左到右是单调递增的.所以如果想在这三个里面找下一个最大值是不可能的.因此我们需要找一个dip point
        在index 1出现了一个下降点. 所以这个是我们第一个需要找到的indx 2) 我们在找到这个index之后想要把这个2换成稍微比它大一点点的value,那么从3，2，2中找,只有3符合这个可能性因此我们需要调换
        index1和index2的value, 最后我们把index1后面的array进行反转就可以得到答案,因此我们知道后面的value是单调递增的,因此进行反转就能达到最小的序列
        """
        i = len(nums)-2
        while i >=0 and nums[i] >=nums[i+1]: # 注意是>= 因为相等的情况也不能进行rearrange
            i-=1
        print(i) 
        if i >=0:
            # 第二步：从右向左找到 nums[i] 右边最小的大于 nums[i] 的数 nums[j]
            j =  len(nums)- 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]