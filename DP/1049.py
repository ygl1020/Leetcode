#这里让你求分割完两个子数组子数组之间的最小和是多少
def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        这题和416数组分割成两个子数组的问题是类似的,416要求你判断是否可以分割为两个和相同的子数组,这里让你求分割完两个子数组子数组之间的最小和是多少
        那么我们的思路就是想尽量分割为两个子数组的和都靠近target的值,然后求在dp[target]里面能装的最大值是多少,最后我们用另一个数组的和减去dp[target]求差
        """
        target = sum(stones)//2
        dp = [0] * (target+1)
        for i in stones:
            for j in range(target,-1,-1): #for j in range(target,-1,-1):
                if i <=j:
                    dp[j] = max(dp[j],dp[j-i]+i)

        return abs(sum(stones)-dp[target] - dp[target]) # error abs(dp[target] - (sum(stones)-target))