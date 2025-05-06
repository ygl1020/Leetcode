#704
"""
需要array确保是有序的 最好是replicate

"""
def search(self, nums: List[int], target: int) -> int:
    """
    这次重新温习了一遍binary search的循环不变量,如果是一开始左右小标的定义是左闭右闭那么后面的while循环和mid下标的跟新也要根据这个predefined区间来选择.eg 如果是左闭右开 都么表明我们不考虑mid==len(nums)的情况,
    所以while条件是while left<right 后面下边的更新,当nums[mid] > target 说明target在左区间我们需要一定right下标为mid,所以直接right=mid(因为不需要考虑在mid的情况),
    如果nums[mid] < target,那么target在左区间,这时更新left的下标为mid,然后left=mid+1,因为我们需要准寻左闭右开的原则,mid的下标已经不考虑了我们考虑mid+1的情况
    
    """
    left, right = 0, len(nums) #左闭右开
    while left <right: #所以不需要考虑left==right的情况
        mid = left + (right-left)//2
        if nums[mid] > target: #target在左区间 直接移动right下标为mid, 我们不考虑mid下标的情况
            right = mid 
        elif  nums[mid] < target:#target在右区间 直接移动left下标为mid, 我们不考虑mid下标的情况,为了保持左闭右开我们需要check mid+1
            left = mid+1
        else:
            return mid
    return -1