##在一个sorted rotated array里面找到数组里面的最小值
def findMin(self, nums: List[int]) -> int:

        """
        eg:[3,4,5,1,2]
        如果使用binary search算法,我们每次循环中nums[mid]大于当前range中的第0个index-->nums[mid] >= nums[l]那么说明当前的index(mid)在左边的数值更大的array,因为
        如果rotate了数组,我们可以保证以index2为分界线的左边array的数值一定是大于右边的,因为这个情况时我们需要向右搜索, 当nums[mid]小于当前range中的最后一个index
        -->nums[mid] <= nums[l],我们需要向左搜索,因为我们已经发现有一个数值是小于nums[mid]的. 最好当我们的range范围中的数组不存在rotated array时,我们直接对比当前的
        res和当前range中的nums[l]就可以得出最小元素
        """
        res = nums[0]
        l,r = 0, len(nums) -1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            mid = (r+l) //2
            if nums[mid] >= nums[l]:
                l = mid +1
            else:
                r = mid -1
            res = min(res,nums[mid])
        return res