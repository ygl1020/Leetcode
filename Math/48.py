# 旋转矩阵
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        这题思路时从外层开始进行rotation,每一层的更新itration为l指针-r指针的范围. 即如果是4*4的矩阵最外层就是更新3次. 然后每一个rotation里面我们需要滚动的过更新四个方位的value.
        为了简洁的代码我们先临时存储左上角的value,然后先更新左上角,然后左下角,右下角,右上角的vlaue. 因为每一层的rotation需要进行多次,每次rotation更新结束我们需要移动index,这个indx
        就是根据for循环里面的i来定的
        """
        l,r = 0, len(matrix)-1  
        while l <r: # control when the full rotation is done
            for i in range(r-l): # control how many rotation with a circular layer
                top,down = l,r 

                topLeft = matrix[top][l+i] # save the topLeft right
                matrix[top][l+i] = matrix[down-i][l] #update topLeft
                matrix[down-i][l] =matrix[down][r-i] #update buttonLeft
                matrix[down][r-i] = matrix[top+i][r] # update buttonRight
                matrix[top+i][r] = topLeft # update topRight
            # after finish rotating that layer, we will start rotating inner layer
            l+=1 
            r-=1