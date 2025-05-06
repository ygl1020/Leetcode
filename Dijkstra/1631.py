def minimumEffortPath(self, heights: List[List[int]]) -> int:
    """
    这题需要判断用稀疏图,因为边的数量明显小于格子平方的数量,否者会超时,然后就是按照template的稀疏图进行修改,有四个方向,然后每个方向需要找最大的effert,然后和dist里面的effert比较更新最小值,然后入堆
    
    """
    r,c = len(heights), len(heights[0])
    direction = [(0,-1),(0,1),(-1,0),(1,0)] # 四个方向
    dist = {(i,j):float('inf') for j in range(c) for i in range(r)} # 创建一个dict,key是每一个格子的方位,value为从(0,0)出发到当前格子的最小minimum effort(maximum absolute difference)
    dist[(0,0)] = 0 #从(0,0)出发所以effert为0
    h = [(0,0,0)] #创建一个最小堆,分别代表miminum effert, row, col
    while h:
        dx, row,col = heappop(h)
        if dx > dist[(row,col)]: #确保我们只考虑minimum effert的情况,如果出现了每次出堆的情况
            continue
        for i,j in direction: #因为有四个方向
            if 0<= row+i< r and 0<=col+j<c: #确保当前的格子在范围之内
                max_height = max(dx,abs(heights[row+i][col+j]-heights[row][col])) #找到maximum的abs height diff
                print(max_height,dist[(row+i,col+j)])
                if max_height < dist[(row+i,col+j)]: #对比dist当中的minimum和当前的minimum 并更新最小值
                        dist[(row+i,col+j)] = max_height
                        heappush(h,(max_height,row+i,col+j)) #把当前的位置入堆
    return dist[(r-1,c-1)] 