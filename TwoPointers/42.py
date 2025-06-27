#计算被困住的water有多少
def trap(self, height: List[int]) -> int:
        """
        解题思路用brute force就是两层for循环.第一层for循环遍历每一个element,第二层for循环遍历当前element左右两边的最大值.然后用公式
        min(leftMax,rightMax)-height[i], 注意这里的差可能为负数,所以要多一个额外的if判断. 然后最坏的可能性是第二层for循环每次都要
        遍历一遍整个height数组,所以时间复杂度是n*n

        optimal two pointers
        通过对比当前左右指针找到更小的那个指针,然后我们移动更小的指针. 之后再更新最大值. 这里先移动指针再更新最大值最后进行计算是因为
        1) 我们不希望计算左右两个boundray的情况 2) 我们需要保证左右两边的最大值都是最新的最大值,另外就是当我们把最大值的取值再(leftMax,height[j])
        进行对比时,如果leftMax小于当前的height[j],下面进行res+= maxLeft-height[l]也不会得到负数
        """
        # brute force o(n^2) 
        # if not height:
        #     return 0
        # res = 0
        # for i in range(len(height)):
        #     leftMax,rightMax =0,0
        #     for j in range(0,i):
        #         leftMax = max(leftMax,height[j])
        #     for j in range(i+1,len(height)):
        #         rightMax = max(rightMax,height[j])
        #     cur = min(leftMax,rightMax)-height[i]
        #     if cur <=0:
        #         cur = 0
        #     res += cur
        # return res

        # two pointer
        if not height:
            return 0
        res = 0
        l,r = 0,len(height)-1
        maxLeft, maxRight = height[l], height[r]
        while l<r:
            if maxLeft<=maxRight:
                l +=1
                maxLeft = max(maxLeft,height[l])
                res+= maxLeft-height[l]
            else:
                r -=1
                maxRight = max(maxRight,height[r])
                res+= maxRight-height[r]
        return res
