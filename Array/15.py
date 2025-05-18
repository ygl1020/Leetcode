# 找到三个element,三个元素的和要等与0
def threeSum(self, nums: List[int]) -> List[List[int]]:
        # map的写法不太好做去重
        # index = {}
        # res = []
        # for i in range(len(nums)):
        #     index[nums[i]] = i
        # for i in range(2,len(nums)):
        #     tmp = nums[i]
        #     for j in range(0,i):
        #         target = -tmp
        #         tmp2 = target - nums[j]
        #         if tmp2 in index and (index[tmp2] <i) and index[tmp2] !=j:
        #             res.append([tmp,tmp2,nums[j]])
        # return res
        
        # two pointers
        """
        先对数组排序,然后两个循环,第一个for循环固定一个值,然后后面的hwile循环用双指针.当total的值大于0,那么就移动右指针,当total的值小于0就移动左指针.当total等于0就把三个数
        放入res数组.需要注意的是这里的去重需要对i,left,right三个地方都做去重.另外双指针的条件不可以包括left==right,这样也可能造成重复
        注意i的去重时要确保i>0, 然后左右指针的去重需要确保l<r这个条件
        """
    
        res =[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >0:
                return res
            if i >0 and nums[i] == nums[i-1]: # 需要确保i>0,否者的话当 nums = [0,0,0]就会漏掉这个答案
                continue
            left, right = i+1, len(nums)-1
            while left < right: # 注意这里不能用等于,因为left和right如果相同,然后total又满足条件的话会出错
                total = nums[i] + nums[left] + nums[right]
                if total >0:
                    right -= 1
                elif total <0:
                    left +=1
                else: # 不要忘记left和right 也要做去重
                    res.append([nums[i],nums[left],nums[right]])
                    # remove duplicate for nums[right] == nums[i-1]
                    while right > left and nums[right] == nums[right - 1]:  #注意不要忘记l<r这个条件
                        right -= 1
                    # remove duplicate for nums[left] == nums[left+1]
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    left +=1
                    right -=1
        return res
