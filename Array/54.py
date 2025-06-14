def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    """
    我们先遍历top row然后right col之后接down row以及left col.每次遍历完一行或者一列之后需要shirnk square的size,通过更新l,r,top,down的value.然后需要注意的细节是1)r,down的初始化要len-1,
    因为后面的for循环会用的l,down的值,如果不-1就会out of range, 然后后面调用l,down的时候记得+1来确保全部的value都能被取到 2)while循环的条件是l<=r and top<=down 3)再在while循环的中间需要
    再次判断while循环的条件
    """
    l,r = 0 ,len(matrix[0])-1
    top,down = 0, len(matrix)-1
    res = []
    while l <= r and top<=down: #我们需要判断两个pair的情况来确保如果只有一行或者一列的数据时我们不会处理完一行或者一列之后不会继续进行for循环,否者就会报错out of index
        for i in range(l,r+1): # 这里r+1,因为我们前面r的index初始化为len(matrix[0])-1, 所以要加1才能遍历到最后一列的元素
            # print(l,r+1)
            res.append(matrix[top][i])
            # print('1',matrix[top][i])
        top+=1
        for i in range(top,down+1): #和r+1相同的道理
            res.append(matrix[i][r])
            # print('2',matrix[i][r])
        r-=1
        if not (l <= r and top <=down): #再遍历完top row和 right col之后我们的外层已经缩小了,因此我们需要判断(l <= r and top <=down)的条件来确保不会把重复的element进行遍历
            break
        print(l,r,top,down)
        for i in range(r,l-1,-1):
            res.append(matrix[down][i])
            # print('3',matrix[down][i])
        down-=1
        for i in range(down,top-1,-1):
            res.append(matrix[i][l])
            # print('4',matrix[i][l])
        l+=1
        # print(l,r,top,down)

    return res