# 查看一个interval数组里面有没有overlap的interval
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    """
    先把intervals数组按照第一个起始index进行排序,然后遍历intervals数组对比最新进入unique数组里面的interval的结束index和当前interval的起始位置来判断是否有overlap
    """
    if len(intervals) <=1:
        return True
    intervals.sort(key=lambda x: x[0])
    unique = [intervals[0]]
    for i in intervals[1:]:
        lastEnd = unique[-1][1]
        if i[0] <lastEnd:
            return False
        unique.append(i)
    return True