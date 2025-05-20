# find the smallest element i where it's digits value adds up to i
def smallestIndex(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(0,len(nums)):
            s = str(nums[i])
            total =0
            for j in s:
                total += int(j)
            if total ==i:
                res = min(i,res)
        return res if res != float('inf') else -1