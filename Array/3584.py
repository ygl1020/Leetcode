# 求一个数组寻找一个中固定长度m的子序列,子序列可以不连续,求所以子序列中第一个vlaue和最后一个value最大的乘积
def maximumProduct(self, nums: List[int], m: int) -> int:
        """
        我们需要从nums里面选取m个element组成一个subsequence.这个subsequence的第一个value乘以最后一个value的值需要为能找到最大值.当我们知道了m的vlaue,那么
        我们就可以确定m的最小的end index, 之后我们要做的就是不断向后一定end index同时记录前面start index的所有取值中的最大值和最小值,这样我们就可以算出以当前
        end index结尾所有得到的最大值,然后在所有最大值里面我们需要取一个最大值. 另外需要注意的是这里subsequence的取值是有序的,但不是连续的
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

print(".".join(["leetcode","com"]))