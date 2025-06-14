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
    
     
        """
        这题的具体思路是一定先把interval按照最左边的value进行排序,然后我们遍历interval里面的元素,对比最新放入res数组的末端和当前interval 元素的初始端
        判断他们是否overlap,如果有overlap就更新res[-1][1]-->最后放入res数组的末尾节点(因为排序后我们可以确保开始节点一定是最小的所以只需要更新末尾的最大节点).
        如果没有overlap我们就直接把interval元素放入res
        我们一开始就放入第一个元素再res里面是为了防止一些edge case
        """
        intervals.sort()
        res = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd,end)
            else:
                res.append([start,end])
        return res