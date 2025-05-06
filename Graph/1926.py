def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    """
    这体的思路是我们我们把棋子的下一步的可能性分为上下左右四个方向,然后我们不会走去过的路径,也不会走出迷宫的范围,以及如果新的方向不是无障碍的话我们也不走
    每走一步我们会把step+1 最后当我们走到了围墙的边缘并且这个点不是entrance的情况下我们就返回steps 否则没有路径我们返回-1
    比较巧的是这里direction是怎么设计的,queue里面放入一个数组,数组里面是元组,然后元组里面是3个参数,row,col,steps.放进元组是因为我们不希望这三个数组进行改变,
    """
    def nearestExit(maze, entrance):
        m, n = len(maze), len(maze[0]) 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 四个移动方向：右、下、左、上
        queue = deque([(entrance[0], entrance[1], 0)])  # 队列中存储 (row, col, steps)
        visited = [[False] * n for _ in range(m)]  # 初始化 visited 数组
        visited[entrance[0]][entrance[1]] = True  # 标记入口为已访问

        while queue:
            row, col, steps = queue.popleft()

            # 检查当前节点是否是出口（边缘位置且不是入口）
            if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and (row != entrance[0] or col != entrance[1]):
                return steps

            # 遍历四个方向
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # 检查新位置是否在迷宫范围内、是否是空地、是否未被访问过
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.' and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True  # 标记为已访问
                    queue.append((new_row, new_col, steps + 1))  # 将新位置加入队列，并增加步数

        # 如果没有找到出口，返回 -1
        return -1
    
    return nearestExit(maze, entrance)