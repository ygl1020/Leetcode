# 215. Kth Largest Element in an Array 
def findKthLargest(self, nums: List[int], k: int) -> int:
        # method 1 brute force
        # nums.sort()
        # return nums[-k]
        
        # method 2 min heap, n+klog(n)
        # mini_heap=[]
        # for idx,v in enumerate(nums):
        #     mini_heap.append((-v,idx))
        # # initialize heap
        # heapq.heapify(mini_heap)
        # # pop out biggest k value
        # for i in range(k):
        #     v,idx = heapq.heappop(mini_heap)
        # return -v

        # method 3 maintain topk mini heap, n+nlog(k)
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in nums[k:]:
            if i > min_heap[0]:
                heapq.heappushpop(min_heap,i)
                # min_heap[0] = i 错误的写法,直接replace min_heap[0]但是没有保证heap的integrety
        return min_heap[0]