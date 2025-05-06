#给定一个ratings数组,规定每一个index需要最少一个candy.并且ratings[i]>rating[i-1]的话rating[i]得到的candy数量要大于i-1.求最少需要多少个candy
class Solution:
    #正确的代码
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        res = [1]*len(ratings)
        for i in range(0,len(ratings)-1):
            if ratings[i+1] >ratings[i]: 
                res[i+1] = res[i]+1
        # print(res)
        for i in range(len(ratings)-2,-1,-1): #不是range(-2,-1,-1)
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i+1]+1,res[i]) 
        return sum(res)  
    
    #错误代码-->没有考虑如果有多个minimum分割点会出现错误的问题. eg: [1,3,2,2,1], 从左1开始切割,左边为0，右边为4 所以错了
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        start_value = min(ratings)
        start_idx = ratings.index(start_value)
        left = ratings[:start_idx+1][::-1]
        right = ratings[start_idx:]
        total_left = self.count_canday(left,1)
        total_right = self.count_canday(right,1)
        print(total_left,total_right)
        return total_left+total_right+1
    def count_canday(self,ratings,min_canday):
        curCandy = min_canday
        total =0
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                curCandy+=1
                total+=curCandy
            elif ratings[i+1] == ratings[i]:
                total+=1
            else:
                curCandy-=1
                total+=curCandy
        return total 
# a = [1,2,3,4,5]
# for i in range(len(a)-2,-1,-1 ):
#     print(a[i])
    
# print([1*3])