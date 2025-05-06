#给定一个无重复值的数组,找到所有的排列可能性,不可以出现重复的可能
def permute(self, nums: List[int]) -> List[List[int]]:
        """
        这里其实和求组合以及子集的去重不太一样,再求组合中我们用startindex来确保每次取值会从当前回合的下一个值开始,再491中我们求递增序列的无重复子集.那里我们采用的是树层的去重,但因为
        我们不可以排序数组,所以不能通过if startindex >i and nums[i]==nums[i-1]来去重,我们再每一层最开始的时候初始化一个数组,然后把当前层遍历过的node都放入数组.
        这题的话我们不需要考虑去重,因为题目说了数组中没有重复值.我们需要used的回溯是因为返回到上层root节点继续向右探索的时候需要把used回复到当前层一开始的状态,否者我后序得到探索就会被遗漏
        """
        if not nums:
            return []
        path,res,used = [],[],[0]*len(nums)
        def backtracking(nums):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]==0:  
                    used[i]=1
                    path.append(nums[i])
                    backtracking(nums)
                    path.pop()
                    used[i] =0
        backtracking(nums)
        return res
    
    
adj = {}

# sort by the destination alphabetically
# 根据航班每一站的重点字母顺序排序
tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets.sort(key=lambda x:x[1])

# get all possible connection for each destination
# 罗列每一站的下一个可选项
for u,v in tickets:
    if u in adj: adj[u].append(v)
    else: adj[u] = [v]
print(adj)




adj = {}

# sort by the destination alphabetically
# 根据航班每一站的重点字母顺序排序
tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets.sort()
# get all possible connection for each destination
# 罗列每一站的下一个可选项
for u,v in tickets:
    if u in adj: adj[u].append(v)
    else: adj[u] = [v]
print(adj)

# tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets.sort()
# print(tickets)
{'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']}
{'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}