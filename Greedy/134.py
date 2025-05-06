#跟你两个数组gas和cost,然后找到哪一个index开始可以跑完全程
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        这题的解题思路很巧妙.注意的解题方法是如果curSum的值小于0那么我们肯定如果这个input有解就一定会在当前i+1的位置开始.然后根据这个原理我们只需要遍历一遍
        数组,然后再每一个回合更新curSum和totalSum.如果curSum<0那我们就更新start, 否者最后判断totalSum的值.因此如果gas数组-cost数组为负数就表明肯定没有解
        """
        start,curSum,totalSum = 0,0,0
        for i in range(len(cost)):
            curSum += gas[i]-cost[i]
            totalSum += gas[i]-cost[i]
            if curSum<0:
                start=1+i # 应该是1+i而不是 start+=1 因为我们只有再curSum<0的时候会更新start,但我们不知道i的值是多少,start+=1不能正确代表当前i的值
                curSum = 0
        if totalSum<0:
            return -1
        else:
            return start