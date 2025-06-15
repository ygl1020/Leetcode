# 求一个数组寻找一个中固定长度m的子序列,子序列可以不连续,求所以子序列中第一个vlaue和最后一个value最大的乘积
def maximumProduct(self, nums: List[int], m: int) -> int:
        """
        因为这个并没有要求subsequence需要连续,所以indx j 可以考虑 index j-m+1之前的全部的值用for循环的j来确定末尾的index, 然后我们记录当前末尾indx前面出现的最大值和最小值,不断更新这个nums[j] 和min以及max的乘积来获取最大的结果
        """

        n = len(nums)
        max_val, min_val = -inf, inf           # best first-element candidates
        best = -inf                            # best product seen so far
    
        for j in range(m - 1, n):
            i_new = j - m + 1                  # index that just became eligible
            v = nums[i_new]
    
            if v > max_val: max_val = v
            if v < min_val: min_val = v
    
            best = max(best,
                        nums[j] * max_val,
                        nums[j] * min_val)
    
        return best  
        
        # brute force solution with time out limit
        # if m == 1:
        #     # only one element, product is square of any number
        #     return max(x * x for x in nums)
    
        # n = len(nums)
        # max_product = float('-inf')
    
        # # Try all i, j pairs such that j > i and j - i + 1 >= m
        # for i in range(n):
        #     for j in range(i + m - 1, n):
        #         product = nums[i] * nums[j]
        #         max_product = max(max_product, product)
    
        # return max_product
