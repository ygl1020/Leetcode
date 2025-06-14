def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        遍历interval里面的所有元素 然后可以把问题拆分成三种情况,情况1: newInterval再元素的左边,这时我们知道一定没有interval比newInterval小,
        所以先把newInterval放入数组,然后之间把interval中剩余的元素加进res数组 2) newInterval再元素右边,那么我们先把元素放入res数组,然后继续遍历
        3) newInterval和元素有overlap,我们需要更新newInterval的边界. 这时需要注意的是我们得出res数组有两种可能性,第一种是通过第一个if情况得出的
        然后有可能这个if再for循环中不会被触发,那么我们就需要把newInterval放入res数组.因此需要再结束fort循环之后运行res.append(newInterval)
        """
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                                min(newInterval[0], intervals[i][0]), 
                                max(newInterval[1], intervals[i][1])]
                print(res)
        res.append(newInterval)
        return res