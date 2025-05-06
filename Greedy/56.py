#给你一个二维数组,然后每一个value代表from intger to inter.让你找到所有没有overlap的区间范围
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        我的思路是需要先把数组排序.然后我们从第intervals第二个元素开始遍历数组.如果当前遍历元素的intervals[i][0] >end or intervals[i][1] <start--?代表这个元素
        不再我们之前的数组范围内.我们就直接把之前的数组放入结果.然后更新start和end为当前的元素value. 其他条件的话就表明当前元素和之前的区间范围有overlap，所以我们
        直接更新start = min(start,intervals[i][0])和end = max(end,intervals[i][1]).最后for循环结束我们把最新的这个start和end interval数组放入res.

        1)我们需要sort数组
        2）start和end是动态更新的根据之前的interval是否包含当前的interval情况
        """
        intervals.sort()
        print(intervals)
        res = []
        start,end = intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if  intervals[i][0] >end or intervals[i][1] <start:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                start = min(start,intervals[i][0])
                end = max(end,intervals[i][1])
        res.append([start,end]) # 记住要把最后一个start,end放入res数组.因为for循环结束之后的最后一个数组再for循环中不会被放入res中
        return res