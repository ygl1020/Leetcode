def jump(self, nums) -> int:
        """
        这题比之前55题难不少.具体原因在于之前的题目我们只需要判断能不能到终点.这题的话我们需要记录到达终点的最小步数.那么思路就是以index0为起点,然后遍历以当前节点能够到
        的所有下一个节点.在这个过程中收集下一步节点所能到达的最远距离.如果最远距离大于或等于nums末尾节点，那么我们就可以判断下一次跳跃可以到达终点.因此return count+1
        否者我们就count+=1.注意这里while循环的i是不变的一直等于0, 然后for循环的i代表的是从0到cover的所有元素.我们可以把for循环看作是下一次跳跃能到达的最远距离
        """
        if len(nums)<=1:
            return 0
        steps,cover =0,0
        i = 0
        while i<=cover:
            # steps+=1 # steps的更新一定是在for循环之后,因为for循环遍历的是再下一个回合中我们能到达的最大cover范围,只有当for循环结束当前step才算完成
            for i in range(i,cover+1): # 这里的range不是(i,i+nums[i]+1)，我们要先process nums[i]然后再更新cover的value,如果是用i+nums[i]+1就跳过一个step直接更新cover了
                cover = max(cover,i+nums[i])
                if cover >= len(nums)-1:
                    return steps+1
            i+=1
            steps+=1