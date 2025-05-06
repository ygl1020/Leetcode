#再一个nums数组里求最大的wiggle数组
def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        这题的思路特别的精巧,大体的解题思路是我们定义一个pre和cur来代表pre difference和curdifference.然后根据题意对wiggle sequence的定义可以得到公式
        (pre<0 and cur>0) or(pre>0 and cur<0)我们就total+=1.那么如果遇见平坡数组怎么半呢?eg: 3,7,7,7,5? 这题答案是3所以我们只需要取最后一个7,因此当pre=0 and cur<0
        我们也要记录.同理cur大于0的情况.因此更新公式(pre<=0 and cur>0) or(pre>=0 and cur<0). 
        那么遇见len(nums)<=0怎么办呢？我们需要至少3个value才能计算pre和cur--->我们可以延长第一个index的值,eg:1,2--> 1,1,2 这样只需要把pre初始化为0就可以变相达到目的
        这样的话还有一个问题我们第一个和第二个值可以使用这个公式那么最后一个值不可以,所以我们直接默认total从1开始然后for循环的时候遍历到倒数第二个值就好了.
        还有一个细节是我们pre=cur的更新只能在找到local maximum时.否者如果遇见单调递增的或者递减的nums会出错eg:1,2,2,2,3 如果pre=cur再if条件的外面答案就是3了,但是这里
        答案是2
        """
        if not nums:
            return 0
        pre,cur,total=0,0,1 # 把pre初始化为0来变相延长数组,这样我们就可以从index 0 开始遍历
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            if (pre<=0 and cur>0) or(pre>=0 and cur<0): 
                total+=1
                pre=cur  # pre的更新只需要在遇见变化的节点用来记录新的坡度,这样的话遇见单调坡度就不会出错
        return total