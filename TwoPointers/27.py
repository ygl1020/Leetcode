def removeElement(self, nums: List[int], val: int) -> int:
        """
        26题因为是需要对比前后的值,所以我们一开始左右指针设置为0,1.这题的话因为我们只删除固定的值,所以我们一开始左右指针设置为0,0
        具体解题思路为当right<len(nums)时我们继续while循环,因为当right到了len(nums)-1,代表我们已经遍历了全部的element
        然后里面的逻辑为,当nums[left]!= val时我们nums[right] = nums[left]，然后同时移动left,right往前一个单位
        当nums[left]== val时，我们只移动right指针一个单位，然后进入下一轮的判断.当下一轮的nums[left]还是等于val那么我们就继续移动left,一直到nums[left]!=val然后这时right还在最后更新的index上,
        这时我们就可以直接更新nums[left] = nums[right], 然后移动左右两个指针一个单位
        
        
        """
        slow,fast = 0,0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
                fast+=1
            else:
                fast+=1
                
        return slow #因为left的index一直指向的是非val值的下标,所以可以理解为left的下标就是非val的nums值的个数