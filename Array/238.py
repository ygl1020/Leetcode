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
        res = [0] * len(nums)
        pre = [0] * len(nums)
        post = [0] * len(nums)
        pre[0],post[-1]= 1,1
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]* nums[i-1]
        print(pre)
        for i in range(len(nums)-2,-1,-1):
            print(i,i+1,i+1)
            post[i] = post[i+1]*nums[i+1]
        print(post)
        for i in range(len(nums)):
            res[i] = pre[i]*post[i]
        return res