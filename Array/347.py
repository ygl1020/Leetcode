def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        第一种方式是1)先把每一个元素以及它的出现次数统计出来然后放入一个字典,2）把字典的k,v pair放入一个数组,然后进行排序-->得到一个按照counts从小到大排列的数组 3)我们数组的后面开始移除k次,并把移除的元素
        放入最后的res数组里面. 这样的话最后的结果就是nlogn因为我们把arr数组排序比较花费时间
        """
        #method 1
        # rank = {}
        # arr = []
        # # calculate the frequency
        # for i in nums:
        #     rank[i] = 1+rank.get(i,0)
        # # insert the occurancy of each value inside the arr array
        # for v,c in rank.items():
        #     arr.append([c,v])
        # # sort the arry array in ace order
        # arr.sort()
        # res = []
        # # pop out the element from arry and add them inside the res array
        # while len(res)<k:
        #     res.append(arr.pop()[1])
        # return res
        
        """
        using min heap total time complexcity is n + klogn = n
        """
        # using min heap total time complexcity is n + klogn = n
        # create dict to store counts
        counts = defaultdict(int)
        for i in nums:
            counts[i] +=1
        #initialize heap
        max_count = [(-fre,v) for v,fre in counts.items()]
        heapq.heapify(max_count)
        # pop out the top k element from heap
        res = []
        for i in range(k):  # takes klogn time
            fre,v = heapq.heappop(max_count)
            res.append(v)
        return res
        