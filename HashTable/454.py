# 从四个数组中抽取一个数,找到所有四个数的的组合和为0的可能性
def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 解题暴力解是直接四个for循环嵌套但是这样的话肯定会时间超时,所以可以思考用hash table来解决, 具体思路是是否有nums1和nums2里面的元素相加的和等于 负的nums3和nums4里面的元素相加的和
        #这样的话我们把同时遍历4个array变成了同时遍历两个array来优化时间
        # 定义一个字典,key 是nums1和nums2里面元素可以组合成的和,value可以随便定，然后遍历nums3和nums4看是否字典里有负数的和的key
        seen = {}
        for i in nums1:
            for j in nums2:
                sum1 = i+j
                if sum1 in seen:
                     seen[sum1]+=1
                else:
                     seen[sum1] =1
        res = 0
        for k in nums3:
            for l in nums4:
                sum2 = -k-l
                if sum2 in seen:
                    res +=seen[sum2] # 这里需要用res +=seen[sum2] 而不是res +=1, 因为我们比如seen= {-2:2, 0:1} 然后 nums3和nums4里面的和的组合等于2的次数为1,等于0的次数为2. 我们如果用res +=1就没有考虑到seen里面出现-2的次数为2次,所以等nums3和nums4的元素和为2时,我们有两种组合方案当我们和nums1和nums2结合时,因此每一次回合的可能性是seen[sum2]
        return res