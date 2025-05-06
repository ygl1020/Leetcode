def removeDuplicates(self, nums: List[int]) -> int:
        """
        这题想到了用双指针的写法解,但是代码还是出了问题,其实这个就是用快慢指针,寻要注意的是while循环的条件是当right指针接触到最后一个index时我们就停止循环
        循环的logic是,如果nums[left] != nums[right],移动左指针然后把左指针的value进行赋值,结束后移动右指针,因为右指针的移动是不分nums[left] != nums[right] 或者nums[left] == nums[right]的情况
        所以我们可以直接放在if条件的外面,最后返回left+1,因为left是从0开始的并且left的下标一直指向的是符合条件的num深度最后一个下标,所以符合体条件的nums的个数是index+1
        
        """
        left,right = 0,1
        while right < len(nums):
            if nums[left] != nums[right]:
                left +=1
                nums[left] = nums[right]
            right +=1
        return left+1     