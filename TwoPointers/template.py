#27
def removeElement(self, nums: List[int], val: int) -> int:
        #快慢指针,i代表这新array的非val的value的index, 这题我们用快慢指针来遍历过nums这样的话可以把暴力解法的n^2变成n
        i = 0
        for j in range(len(nums)):
            if nums[j] !=val:
                nums[i] = nums[j]
                i +=1
        return i