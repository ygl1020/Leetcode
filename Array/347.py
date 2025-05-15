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
        method 2, 我们1)先计算每一个元素出现的次数并把元素作为key,出现次数作为value储存再字典里.2)创建一个二维字典buck_arr,字典长度为len(nums)+1-->出现counts最多的可能就是一个元素出现len(nums)次
        然后字典的每一个element--buck_arr[i]是一个字典用来存储所有出现过i次的元素. 3)最后我们从后开始遍历buck_arr-->从大到小的出现次数,然后找到k个出现最多的元素加入res
        """
        # buck_arr = [[] * (len(nums)+1] casued error bc this create 5 reference array and appending to one sublist affects all because they are actually the same list object.
        buck_arr = [[] for _ in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = 1+count.get(i,0)
        print(count)
        for v,c in count.items():
            buck_arr[c].append(v)
        res = []
        print(buck_arr)
        for i in range(len(buck_arr)-1,0,-1):
            for n in buck_arr[i]:
                print(buck_arr[i])
                if n is not None: # 这里不能用if n , 因为这样的话出现了elment为0的情况就会过滤掉这个元素
                    res.append(n)
                if len(res) >=k:
                    return res
        