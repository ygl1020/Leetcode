#给定一个数组和m，n让你求一个子数组然后子数组中的所有元素0的个数最多为m，1的个数最多为n.让你求满足条件的最大子数组长度
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        这题我们把背包看成是二维的,背包容量为m个0和n个1,然后数组里面的每一个元素有对应的重量m',n'当我们可以把当前元素放入背包时,整个元素看作一个物品
        1)dp[i][j], 最大容量i个0和m个1的数组最多可以dp[i][j]个子数组
        2)递归公式和传统的01背包问题一样只不过现在是二位的表达式 dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)-->这里+1很重要,这个1代表element本身
        3）初始化和传统01背包一样都是0
        
        这题是把背包容量转化为2维的数组,分别对应m和n的最大容量. 因此dp数组的含义就是背包容量为m个0和n个1的时候该背包所能放下的最大数组长度为dp[n][m]
        递归公式的话正常一位背包为 dp[j] = max(dp[j], dp[j-i]+i), 这里的话因为是二维数组,所以应该是dp[i][j] = max(dp[i][j], dp[i-ones][j-zeors]+1) 加1的是因为当我们考虑放入数组时先减去所需的重量
        然后因为dp数组表示的是能放入的最大数组的长度，所以加1. dp数组初始化因为dp[0][0]就是0,因为m=0,n=0时能放下的最大长度的数组就是0
        然后这里的话因为背包重量是二维的所有我们需要先计算当前字符串种0，1的数量,然后再用两个for循环来遍历背包
        """
        dp = [[0]*(n+1) for _ in range(m+1)] # 注意这里决定了我们把n定义成col,m定义成row
        for s in strs:
            zeros = s.count('0')
            ones = len(s)-zeros
            print(zeros,ones)
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        print(dp)
        return dp[m][n]