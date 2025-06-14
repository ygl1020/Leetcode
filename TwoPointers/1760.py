#分配所有袋子里的ball,求分配完袋子中的最大值的可能最小值是多少
def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        这题和2064是一样的套路,都是再最大值里面求可能的最小值.brutue force解法是不用双指针,然后采用一个helper 函数来判断如果把每一个bag的ball的数量分配为小于或等于upperLimit,我们最少需要分配
        多少次才能把全部bag的ball都分配完. 然后我们比较这个ops的值和maxOperations,如果ops的值大于maxOperations就说明这个upperLimit太小了,我们需要增加这个upperLimit,反之就需要减少upperLimit
        的值.brute force的time complecity是o(len(nums)*max(maxOperations)), 但因为maxOperations是有序的,我们可以用二分法来进行优化,最后o(len(nums)*logmax(maxOperations))
        """
        def find_minimum(upperLimit):
            ops = 0
            for i in nums:
                ops+= ceil(i/upperLimit)-1
            return ops <=maxOperations
        
        l,r = 1, max(nums)
        res = 0
        while l<=r:
            x = (l+r)//2
            if find_minimum(x):
                r = x-1
                res =x
            else:
                l = x+1
        return res