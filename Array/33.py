#在一个sorted rotated array里面找到一个特定的值,然后返回其坐标,没找到的话返回-1
def search(self, nums: List[int], target: int) -> int:
        """
        回顾一下这题是对sorted 数组进行rotate了,所以我们可以把mid按照在左边的区间和右边的区间进行分类讨论. 当nums[mid] >nums[r]时我们可以肯定mid在左区间,否者如果在sorted数组里面不可能
        出现这个情况. 确定了mid左区间,那么什么时候把左指针向右移动? -->nums[mid] <target or nums[l] >target 其他情况就把右指针向左移动
        当mid在有右区间什么时候把右指针向左移动? --> target < nums[mid] or nums[r] < target
        这题要活用l,r两个区间的值和target作对比来确定移动方向
        """
        l,r = 0,len(nums)-1
        while l <=r:
            mid = (r+l)//2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]: # error1 
                if nums[mid] <target or nums[l] > target:
                    l = mid+1
                else:
                    r=mid-1
            else:
                if nums[mid] >target or nums[r] < target: # error2
                    r=mid-1
                else:
                    l=mid+1
        return -1