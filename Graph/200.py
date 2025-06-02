# 求岛屿数量
def numIslands(self, grid: List[List[str]]) -> int:
    """
    这题的也是求连通图的个数,思路和547类似可以采取dfs,在dfs函数中,如果recursive的过程没有越界并且value的值为"1"那么我们就一直进行下去一直找到全部相邻的"1"的点,然后我们跳回到外面的循环开始进行下一轮的判断
    这题的关键是我们的1)return条件是什么  2)在dfs函数里面我们需要做什么 3)在外围的for loop我们的什么时候ans+1并且进入dfs
    
    "这题的思路是对每一个岛屿的节点开始不断向上下左右四个方向向外延伸，一直到我们发现当前的岛屿已经遍历完成。这个过程就是bfs
        我们需要明确我们bfs中有四个方向的可能，并且我们只便利grid[i][j]=='1'和当前岛屿没有被探索过的情况。最后grid中的每一个
        elememnt我们都需要这样便利一次，但由于们只便利grid[i][j]=='1'和当前岛屿没有被探索过的情况，我们不是在每一个
        节点都会继续invoke bfs-->之前已经遍历过了就会跳过，然后我们count只在bfs被activate的情况加1"
    """
    m,n = len(grid), len(grid[0])
    ans = 0
    def dfs(i,j):
        if i >= 0 and i < m and j >=0 and j<n and grid[i][j] =='1':
            grid[i][j] = 2
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        else:
            return
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value =="1":
                ans +=1
                dfs(i,j)
    return ans


def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j):
            if i >= 0 and i < m and j >=0 and j<n and grid[i][j] =='1':
                grid[i][j] = 2
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            else:
                return
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value =="1":
                    ans +=1
                    dfs(i,j)
        return ans