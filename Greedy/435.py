# 构成一个没有overlap的数组interval求最小需要删除的interval个数让
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        这题如果用贪心的思路解题的话是我们要保证每一个interval的区间足够小,这样我们每次删除的interval就是那些gap大的区间来减少区间删除的次数.如果要保证每次区间的gap最小,我们就需要
        每一个interval尽可能早的结束,这样的话我们就需要看第二个末尾index进行从小到大的排序. 因此我们先把intervals按照第二个index来进行排序,然后遍历每一个element,如果发现
        当前element的startIndex,是>= 最新放入noDuplicate的interval的end index,那么就说明没有overlap,否者我们就需要删除元素-->res +=1 并且不把当前interval放入noDuplicate数组
        """
        # intervals.sort()
        intervals.sort(key=lambda x: x[1]) 
        print(intervals)
        noDuplicate = [intervals[0]]
        res = 0
        for i in intervals[1:]:
            lastEnd = noDuplicate[-1][1]
            print(lastEnd,i[0])
            if i[0] >= lastEnd:
                noDuplicate.append(i)
            else:
                res +=1
        return res