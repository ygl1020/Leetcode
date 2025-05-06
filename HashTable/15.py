def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        这题用一开始我想用hash table来做,先两个for循环计算出所有和的可能,但然后再用一个for循环来看是否在hash tbale里面有满足条件的数,但是卡在怎么去重的步骤上
        所以转换思路用双指针的方法写,一定要先sort数组用双指针的话!!具体思路是用一个for循环先遍历所有的元素,我们需要求nums[i] +nums[left]+nums[right] == 0的数组,并对这些数组进行去重.这题去重的话又分三个维度的去重1)i的去重2)left的去重 3)right的去重
        在for循环中的i代表nums[i],这里我们去重的判断是通过对比nums[i]和nums[i-1]的值. 之后我们在每一个iteration中使用双指针来获取nums[left]和[right]的值,并根据三数之和来不断移动左右指针查找在当前的nums[i]是否有符合条件的组合
        另外注意对于i的去重一定是用i-1的值对比而不是i+1,否者或跳过符合的可能性.eg[-1,-1,1],如果用i+1这个组合就跳过了
        这里需要注意的是当三个去重的操作,一个是当i和i+1的vlaue相同,一个是left指针移动时下一个value相同最后是right指针移动时下一个value相同
        另外即使我们在双指针用了左闭右闭的区间,我们不可以用while left<=right,因为nums[right]和nums[left]不能指向同一个index
        
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >0:
                return res
            # remove duplicate for nums[i] == nums[i+1]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right: # we cannot use left <=right, since we need at least three elements in a combination so nums[left] and nums[right] cannot pointer to the same index
                total = nums[i] +nums[left] +nums[right]
                if total > 0:
                    right -=1
                elif total <0:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    # remove duplicate for nums[right] == nums[i-1]
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    # remove duplicate for nums[left] == nums[left+1]
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    left +=1
                    right -=1
        return res