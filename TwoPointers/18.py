def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        这题我想到了解题思路和15题3SUMS类似,我们只需要在外面套两成for循环然后用双指针的写法来解题
        但是我改代码的时候去重的处理没有做好
        1)我没有在每一个for循环里面都进行去重的判断,
        2)在for循环出重时不应该用: if j > 0 and nums[j] == nums[j+1]:这样的话再最后一个index的时候会超出range,另外这种写法会跳过组合[-1,-1,0,0], target=0 这时这种写法再处理第一个-1时会跳过当前的-1,但是其实这个-1是可以被收录的
        
        有两个细节需要注意,i的range是动态改变的根据j的值所以我们不能用:for i in range(1,len(nums)):
        同理可得去重的判断也是相同的道理:不能用: if i > 1 and nums[i] == nums[i-1]: 要用: if i > j+1 and nums[i] == nums[i-1]:
        """
        res = []
        nums.sort()
        for j in range(0,len(nums)):
            if j > 0 and nums[j] == nums[j-1]:# 去重
                continue
            for i in range(j+1,len(nums)):
                if i > j+1 and nums[i] == nums[i-1]: # 去重
                    continue
                left = i+1
                right = len(nums)-1
                while left<right:
                    total =  nums[j]+nums[i] +nums[left] +nums[right]
                    if total > target:
                        right -=1
                    elif total <target:
                        left +=1
                    else:
                        res.append([nums[j],nums[i],nums[left],nums[right]])
                        # remove duplicate for nums[right] == nums[i-1]
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left +=1
                        right -=1          
        return res