def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums.sort( reverse=True)
        # total,steps =0,0
        # for num in nums:
        #     if num <=0:
        #         continue
        #     total += num
        #     steps+=1
        #     if total >=target:
        #         return steps
        # return 0
        #两个疑问1)为什么这里左闭右开的时候不需要考虑index超出range的问题，2）在977里面我们需要考虑range溢出的问题
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
