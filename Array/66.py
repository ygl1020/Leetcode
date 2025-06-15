#把一个数组的最后一个element进行+1,然后返回更新完之后的数组
def plusOne(self, digits: List[int]) -> List[int]:
        # brute force solution with space more memory required
        # start = ''
        # for i in digits:
        #     start+=str(i)
        # add_str = str(int(start)+1)
        # # print(add_str,type(str))
        # res = []
        # for i in range(len(add_str)):
        #     res.append(int(add_str[i]))
        # return res
        # optimal solution with less space required

        """
        先把digits进行反转,这样的话如果遇见[9,9]这种情况我们只需要再数组的最末端append 1就可以了. 先设置两个variable分别代表需要增加的value 1和index i=0
        当我们需one=1时我们继续循环,循环中我们先判断index i是否还在digits的range里面,如果再的话分两种情况1)digits[i]为9那么我们就需要把digits[i]变为0,然后对它之前的数
        进行+1, 如果digits[i]不等于9，那么我们可以直接对digits[i]进行+1,然后把one变成0. 当i>=len(digits),我们说明我们遇见了[99]这种情况,那么我们再最后的时候再digits的末尾
        append(1)进去,然后把one的value设置为0.需要注意每次while循环的logic结束后需要更新i的value. 最后return 反转的digits就好了.         """
        digits = digits[::-1]
        one,i = 1,0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] =0
                else:
                    digits[i] = digits[i] +1
                    one = 0
            else:
                digits.append(1)
                one =0
            i+=1
        return digits[::-1]