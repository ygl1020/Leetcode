def generateMatrix(self, n: int) -> List[List[int]]:
    """
    这题的思路是定义四个边界值,上下左右分别为:0,n-1,0,n-1,和n*n的数组, 开始while num <= target循环,条件是这个因为我们每一次for循环num+=1,所以我们for循环的次数总共为n*n次,因为当num==target时我们遍历完全部的元素停止循环
    for循环里面要注意每一次的边界,这里我们用的是左闭右闭的边界, 每一次for循环因为我们经过了一个element所以num+=1,然后当结束当前那条边的for循环,我们把对应方向进行更新,up+=1, down-=1, right-=1, left+=1
    另外num从1开始,因为每一次我们之后把num的值进行更新
    最后我们直接返回matrix

    """
    # create a n * n matrix
    matrix = [[0] *n for _ in range(n)]
    up,down,left,right = 0,n-1,0,n-1
    num,target = 1,n*n
    while num <= target:
        for i in range(left,right+1): #left to right from top
            
            matrix[up][i] = num
            num +=1
        up+=1
        for i in range(up,down+1): # up to down from right edge
            matrix[i][right] = num
            num +=1
        right-=1
        for i in range(right,left-1,-1): # right to left from down edge
            matrix[down][i] = num
            num +=1
        down -=1
        for i in range(down,up-1, -1): #  down to up from left edge
            matrix[i][left] = num
            num +=1
        left +=1
    return matrix