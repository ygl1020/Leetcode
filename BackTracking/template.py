# 77	Combinations
def combine(self, n: int, k: int) -> List[List[int]]:
    """
    第一题回溯的题目 首先根据回溯三部曲来思考解题思路。1)递归函数的参数需要什么，返回的值是什么 2)递归的终止条件是什么 3)在每一层递归的逻辑是什么。 
    首先 1)我们需要把n,k,starIndex三个参,n代表我们可取值的合集k代表我们迭代的深度 然后startindex可以让我们之后下一个迭代步骤时我们取值从哪里开始取 
        2)这里的话我们在触及到leaf时搜集并开始回溯的过程 
        3)在一层递归中,我们把当前的值放入path当中。
        这里我一开始写的时候在if条件里面append的是path本身而不是它的copy,这样有一个问题是当path改变时那么res里面append的值也会改变。 
        然后就是for循环的range参数,我一开始用的是(1,n+1)但是我不应该放固定的1在这里,因为当我们拿取了第一个element时,下一个level我们希望从他的下一个数开始取值,所以应该用startIndex。
        3)之后就是递归时backtracking()里面的参数,我不应该用stratIndex+1, 应该用i+1, 这里的理由和第二条一样 
        另外我们需要startIndex的原因是因为当我把递归下一个回合时我们希望从之前那个回合的下一个值开始，所以我们需要一个index来获得这个信息
    """
    path,res = [],[]
    def backtracking(n,k,startIndex):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(startIndex, n+1):
            path.append(i)
            backtracking(n,k,startIndex+1)
            path.pop()
    backtracking(n,k,1)
    return res

# 39	Combination Sum
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    这里做一个小总结,一般如果是在一个合集里面找combination,我们都会需要一个startindex的参数在递归函数里面,如果是多个合集的话就需要,然后这题和216不太一样,因为我们没有固定的for循环层数K,所以这样的话我们就需要考虑放入一个total的参数,
    然后if的返回条件是当total == target,那么path加入res并return 或者total > target那么直接return 另外我想说一下一般for循环里面第一个取值都是startindex,然后再后面调用递归函数时使用i,因为如果把i换成startindex那么下一次循环的开始取值和上一个循环的一样的,
    但是如果换成i的话是每一次开始的值都是上一次循环的下一个值。最后一个疑问时为什么我们需要total -= candidates[i]? 理由是当total > target时,我们会触发retur，然后在开始下一个递归时我们应该先把上一次的node value减去,否则的话total的值就不正确了

    """
    res, path = [],[]
    def backTracking(candidates, target,total,startIndex):
        if total>=target:
            if total ==target:
                res.append(path[:])
                return 
            else:
                return 
        for i in range(startIndex,len(candidates)):
            total += candidates[i]
            path.append(candidates[i])
            backTracking(candidates, target,total,i)
            total -= candidates[i]
            path.pop()
    backTracking(candidates, target,0,0)
    return res



# 47 Permutations 排列

def permute(self, nums: List[int]) -> List[List[int]]:
    """
    排列问题需要和组合问题合起来讨论,在排列问题时,我们考虑的重点在于顺序所以[1,2] 和[2,1]是不一样的.再组合中,为了避免这种情况发生我们用startIndex来解决这个问题,那么这就说明我们在排列问题中是不需要startIndex的.这样的话另一个问题是我们如果避免使用重复的值呢?
    这时我们需要引用used 数组,当used[i] is False 那么就意味着当前的value没有被使用过,否者我们就跳过当前的值
    1) 递归函数中需要什么参数? ---> nums, used数组来传递取值的信息
    2) 什么时候开始return呢? --> 当len(path) == len(nums)
    3) 每一个iteration我们需要做什么? 第一判断used[i]是否为true,  第二把used[i]变成true, nums[i]加入到path, 第三开始递归函数 第四开始回溯
    """
    res, path,used = [],[],[False]*len(nums)
    def backTracking(nums,used):
        if len(path) >= len(nums):
            res.append(path[:])
        for i in range(0,len(nums)):
            if used[i] is True:
                continue
            used[i] = True
            path.append(nums[i])
            backTracking(nums,used)
            used[i] =False
            path.pop()
        return
    backTracking(nums,used)
    return res

chessboard = ['.' * 4 for _ in range(4)]  
chessboard