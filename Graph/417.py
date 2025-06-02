def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        我一开始的想法是对每一个格子用dfs,然后用不需要用visited来记录走过那些节点,这样的话dfs的time complecity是M*N,然后我们有M*N个格子,所以时间复杂度是(M+N)^2
        然后下面是优化过后的算法,我们从board出发-->board肯定可以流入海洋,所以我们记录哪些格子可以到达board.通过dfs我们分别计算出pacific和atlantic的结果.最后我们遍历一遍
        格子看哪些格子出现在了visited_p和visited_a的结果集里面.dfs的逻辑是我们当前格子如果越界了,或者已经到过了,以及当前的heigh是<preHeight的话就return.不然我们就把当前格子
        放入visited 元组,然后进行四个方向的dfs
        """
        if not heights:
            return []
        res = []
        ROW, COL = len(heights), len(heights[0])
        visited_p, visited_a = set(), set()

        def dfs(r,c,preLevel,visited):
            if ((r,c) in visited) or r <0 or c<0 or r >=ROW or c>=COL or heights[r][c]<preLevel:
                return
            visited.add((r,c))
            preLevel = heights[r][c]
            dfs(r+1,c,preLevel,visited)
            dfs(r-1,c,preLevel,visited)
            dfs(r,c+1,preLevel,visited)
            dfs(r,c-1,preLevel,visited)
        for c in range(COL):
            dfs(0,c,heights[0][c],visited_p)
            dfs(ROW-1,c,heights[ROW-1][c],visited_a)   
        for r in range(ROW):
            dfs(r,0,heights[r][0],visited_p)
            dfs(r,COL-1,heights[r][COL-1],visited_a)   
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in visited_p and (i,j) in visited_a:
                    res.append([i,j])
        return res