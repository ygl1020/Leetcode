#给你一个nums数组,每一个value代表能跳的最大步数.问你能否到达终点
def canJump(self, nums: List[int]) -> bool:
        """
        这题我一开始的思路是判断每一个分区间里面所覆盖的所有步数是否都会等于0.但是这个想法处理起来比较难实现.比较容易实现的方式是判断步数覆盖的范围.我们用while循环遍历
        整个nums,然后每一个回和我们直接更新cover为最大的步数.当i大于cover时我们停止循环——->代表我们不能到达终点.在遍历过程中如果cover>=len(nums)-->可以到达终点我们
        就返回true
        
        这里需要设置一个cover来代表最长能跳跃的长度.然后我们用循环不断更新这个cover的最大值.注意需要用while而不是for,因为当i>cover时我们知道当前的数组不可能再往前走了
        """
        if len(nums)==1:
            return True
        cover = 0
        i =0
        while i <=cover: 
            cover = max(i+nums[i],cover)
            if cover >=len(nums)-1:
                return True
            i+=1
        return False