def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    """
    这题我的思路是用dfs从rooms[0]开始进行recursive,每次路过一个房间把它对应的visited[cur]标记为1,最后如果visited里面没有0,那么就是全部房间都去过了
    1) 我们需要把什么参数放进dfs函数里面? rooms, cur (代表我门当前正在处理哪一个index在room[cur]里面)
    2) 什么时候结束recursive 返回结果? 在if里面我们可以判断是否有0在visited里面,如果没有那么就说明全部房间都去过了可以直接返回 2: 在for循环里面 如果从rooms[0]开始recursive里面的每一个相连的房间,最后if条件还是没打成也触发返回条件
    3) 在每一个iteration我们需要做什么:我们需要把visited对应的房间进行标记
    
    然后这题我一开始是吧visited[cur] =1放在了for循环里面,这样的话有一个问题当房间里时空的就不会触发for循环,那么我们就标记不了这个房间
    
    """
    visited = [0] * len(rooms)
    res = False
    def bfs(rooms,cur):
        nonlocal visited,res
        visited[cur] =1
        if 0 not in visited:
            res = True
            return 
        for i in rooms[cur]:
            if visited[i] ==0:
                bfs(rooms,i)
    bfs(rooms,0)
    return res
from itertools import count
count_s = 0
while count_s <=10:
    for step in count(1):
        print(step)
        count_s +=1
        print(count_s)