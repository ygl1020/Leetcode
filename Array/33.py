#在一个sorted rotated array里面找到一个特定的值,然后返回其坐标,没找到的话返回-1
def search(self, nums: List[int], target: int) -> int:
        """
        这题最好画一个图,然后把所有的可能性给思考清楚.大的情况可以分为nums[mid]在左边的sorted array当nums[mid] > nums[l]然后在这个if条件里面我们可以分为三总情况1)nums[mid] < target or nums[l] > target-->我们搜索右边的情况, 2)其他情况搜索左边的区间. 第二个大情况时nums[mid]在右边的sorted array, 然后细分三种可能性1)target < nums[mid] or target > nums[r]-->搜索左边
        2）其他情况搜索右边
        """
        l,r = 0, len(nums)-1
        while l <=r:
            mid = (r+l) //2
            if nums[mid] == target:
                return mid
            # left portion segment
            if nums[mid] >= nums[l]:
                if nums[mid] < target or nums[l] > target:
                    l = mid +1
                else:
                    r = mid-1
                print('left',l,r)
            #right portion segment
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid +1
                print('right',l,r)
        return -1