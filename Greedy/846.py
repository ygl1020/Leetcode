#给你一个数组和groupsize.求是否有可能再数组里面构成groupsize个连续的子数组
def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        这题的解题思路为每次都选取当前剩余元素的最小元素为起始点开始构建子数组.因此我们需要先把hand进行排序.然后我们创建一个dict来存储每一个unique value的occurance.之后我们遍历hand数组,如果counts[nums]存在且不为0
        那么它一定是一个sub-array的最小起始元素.因此我们进行下一个for循环,判断从num到num+groupSize的全部元素是否再counts字典里面.如果不存在或者counts[i]==0，那么就说明构建不了数组-->return False
        """
        if not hand or len(hand) % groupSize !=0: # if len(hand) is not divided by groupSize--> return false
            return False
        hand.sort() # sort the array, so we can make sure the starting point of the array always be traversed first 
        counts = {} 
        for num in hand:
            counts[num] = 1 + counts.get(num,0) # a dict to store the occurance of the value
        for num in hand:
            if counts[num]: # if counts[num] exist, then there it must be the starting point of a sub array, then we can see if its following key are existing inside the coutns dict
                for i in range(num,num+groupSize):
                    if i not in counts or counts[i]==0:
                        return False
                    counts[i] -=1
            # else:                         # 如果counts[num]为0或者不存在就不需要进行判断
            #     return False
        return True