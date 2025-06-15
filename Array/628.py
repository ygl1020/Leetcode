#在一个数组中找三个数然后算出最大可能乘积的值
def maximumProduct(self, nums: List[int]) -> int:
        #method1 using sort for 0(nlongn)
        # nums.sort()
        # product1 = nums[0]*nums[1]*nums[-1]
        # product2 = nums[-1]*nums[-2]*nums[-3]
        # print(nums)
        # print(product1,product2)
        # return max(product1,product2)

        #method 2 using for loop to find max1,2,3 and min1,2 for o(n)
        """
        第二种思路时用for循环找到3个max和另外2个min. for循环的逻辑时先判断n是不是大于max1,如果的话就反向先更新max3,max2最后max1. 如果n<=max1，那么就check n是不是大于max2, 相同的逻辑用于max3以及min1，min2
        最后return 两种可能的maximum product
        """
        max1=max2=max3=float('-inf')
        min1=min2 = float('inf')
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >max2:
                max3 = max2
                max2 = n
            elif n>max3:
                max3 = n
            
            if n <min1:
                min2 = min1
                min1 =n
            elif n<min2:
                min2 = n
        return max(max1*max2*max3, max1*min1*min2)