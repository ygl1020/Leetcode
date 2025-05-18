# 让你求不包括当前index的所有其它element的乘积和
def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        # res = []
        # for i in range(0,len(nums)):
        #     product = 1
        #     for j in range(0,len(nums)):
        #         if j ==i:
        #             continue
        #         # print(product)
        #         product = product * nums[j]
        #     res.append(product)
        # return res

        # Prefix and Postfix
        """
        计算nums的prefix和postfix然后根据对应index的值进行相乘
        """
        prefix = [1 for _ in range(len(nums))] 
        backfix = [1 for _ in range(len(nums))] 
        res = []
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
   
        for i in range(len(nums)-2,-1,-1):# 注意这里的range是(len(nums)-2,-1,-1)
            backfix[i] = nums[i+1] * backfix[i+1] 

        print(prefix,backfix)
        for i in range(0,len(nums)):
            res.append(prefix[i]*backfix[i])
        return res