# 给定一个intervals数组,然后根据里面的interval来判断最少需要多少间会议室
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        双指针的解法,我们画图然后可以得到一些思路.具体的解法是先把数组中的开始和结束位置分别放入两个数组并进行排序.然后用两个指针遍历两个数组.当遍历完start数组就可以结束while循环
        然后while循环里面的逻辑是1)当start[l] <end[r]--> count+1代表需要一件会议室, 然后移动l指针并记录最大值 2) 当start[l] ==end[r]时我们count-1代表一个会议结束了然后我们需要
        先移动r指针 3)当当start[l] >end[r]时我们count-1代表先把会议结束,然后移动r指针.

        这里需要注意的逻辑count用了记录实时需要的root然后就是先处理最小的value,如果时start[l]小那就增加会议然后移动l指针, 如果出现了tie,我们需要先结束会议然后更新r指针和减少count
        最后如果start[l]>end[r]. 我们就先结束会议移动r指针以及更新count
        """
        start,end = [],[]
        for i,j in intervals:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        l,r = 0,0
        count,res = 0,0
        print(start,end)
        while l < len(start):
            if start[l] < end[r]:
                count+=1
                res = max(res,count)
                l+=1
            elif start[l] == end[r]:
                count-=1
                r+=1
            else:
                count-=1
                r+=1
        return res