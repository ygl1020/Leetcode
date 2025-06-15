#在一个数组中计算符合条件的trieplet
def specialTriplets(self, nums: List[int]) -> int:
        """
        用defalutdict来创建left,right两个字典.我们先把nums遍历一遍来获取全部element的occurance. 然后在for循环里面,进入for循环我们先在right[nums[j]]中减去一个单位,因为当前的nums[j]时中间的位置,然后我们在left以及right字典里面找符合double_val = nums[j] * 2的元素个数, 把他们的个数进行相乘.我们用count来记录这个乘积然后最后我们需要把当前的nums[j]放入
        左边的字典里面
        """
        from collections import defaultdict

        MOD = 10**9 + 7
        count = 0
        right = defaultdict(int)
    
        # Count frequency of each number to the right of j
        for num in nums:
            right[num] += 1
    
        left = defaultdict(int)
    
        for j in range(len(nums)):
            right[nums[j]] -= 1  # j is no longer in "right"
    
            double_val = nums[j] * 2
            count_left = left[double_val]
            count_right = right[double_val]
    
            count += count_left * count_right
            count %= MOD
    
            left[nums[j]] += 1  # move j into "left" after processing
    
        return count