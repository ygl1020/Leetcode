#977
def sortedSquares(self, nums: List[int]) -> List[int]:
    """
    这题的思路是用双指针,然后找到左右指针的vlaue的绝对值大的数放入新的数组,这里不能先放绝对值小的vlaue.之后我们对比abs(nums[left]) >= abs(nums[right - 1]),并把大的值放入new_list,对应的下标+=1,最后return new_list
    另外就是区间不变量因为这里用的是左闭右开的区间所以while是left<right 并且我们只能取nums[right-1]不能取到nums[right]
    如果是左闭右闭就是left, right = 0, len(nums)-1. while left <=right, nums[right]
    
    """
    new_list = []
    left, right = 0, len(nums)  # right is open (beyond the last index)
    
    while left < right:  # Notice `<` instead of `<=`
        if abs(nums[left]) >= abs(nums[right - 1]):  # Use right - 1
            new_list.append(nums[left] ** 2)
            left += 1
        else:
            new_list.append(nums[right - 1] ** 2)
            right -= 1  # Decrease `right`, keeping it open
    
    return new_list[::-1]  # Reverse to get sorted order