# 给你一个数组,让你求那两个数组之间构造容器可以装最多的水
def maxArea(self, height: List[int]) -> int:
        """
        需要注意一个点,在当前l,r的区间内,如果我们想要找最大值就只可能移动height相对较小的那一个pointer
        """
        if len(height) <=2:
            return min(height) 
        res = 0
        left,right = 0, len(height)-1
        while right>left:
            tmp = min(height[left],height[right]) * (right-left)
            print(tmp)
            res = max(tmp,res)
            if height[left]>= height[right]:
                right-=1
            else:
                left +=1
        return res