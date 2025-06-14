#求再在商店中分配物品数量的最大值的可能最小值是多少
def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        这题的第一步是先理解brute force的解法,这题要求的是再分配完之后最大物品数量的可能最小值是多少. 每一个商店只能分配一种物品
        所以每一个商店可能分配的物品数量为1-max(quantities), 然后我们traverse quantities中每一个物品来计算根据当前分配数量我们最小需要的
        商店数量是多少,如果数量counts<=n, 那么意味着当前分配数量还可以下降,反之意味着数量需要上升. 然后这个过程是brute force是用for循环来解的
        ,但是因为这个数量是有序的数组,因此我们可以用二分法来解题,时间复杂度是o(len(quantities)*logmax(quantities))
        """
        def can_distribute(x):
            counts =0
            for q in quantities:
                counts+=ceil(q/x) # round up, since stores number should be integer
            return counts <= n
        
        l,r = 1, max(quantities)
        res = 0
        while l<=r:
            x = (l+r)//2
            if can_distribute(x):
                r = x-1
                res = x
            else:
                l =1+x
        return res