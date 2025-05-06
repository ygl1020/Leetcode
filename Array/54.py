def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    """
    这题和59题解题思路是一样的,唯一的区别在于需要加一个if的边界条件判断在在每一个for循环里面
    
    """
    m,n = len(matrix), len(matrix[0]) # row, column
    num, target = 1, m*n
    result = [] 
    up,down,left,right = 0, m-1, 0, n-1
    while num <= target:
        for i in range(left,right+1):
            if num <= target:
                result.append(matrix[up][i])
                num+=1
        up+=1
        for i in range(up, down+1):
            if num <= target:
                result.append(matrix[i][right])
                num+=1
        right-=1
        for i in range(right,left-1,-1):
            if num <= target:
                result.append(matrix[down][i])
                num+=1
        down -=1
        for i in range(down,up-1,-1):
            if num <= target:
                result.append(matrix[i][left])
                num+=1
        left+=1
    return result