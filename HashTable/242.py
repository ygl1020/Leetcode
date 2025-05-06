"""
这题有两种解法 第一种是我自己的解法,创建两个dict用来分别记录s和t里面每个元素出现的个数,然后我们遍历len更长的那个dict对比其中的每一个key的值是否和另一个dict相同,不同的话就return Fasle
第二题的解法更巧妙一些,我们通过ord()可以把一个char置换成一个固定的number(0--25对应26个字母)然后每次遇见把对应下标的value+1,然后我们遍历另一个字符串去减去之前那个char所对应的value-1
最后如果里面的值不是0那么就返回false

"""
def isAnagram(self, s: str, t: str) -> bool:
        #method one
        # num_counts = {}
        # num_counts2 = {}
        # for i in s:
        #     if i not in num_counts:
        #         num_counts[i] = 1
        #     else:
        #         num_counts[i] +=1
        # for j in t:
        #     if j not in num_counts2:
        #         num_counts2[j] = 1
        #     else:
        #         num_counts2[j] +=1
        # if len(num_counts) <len(num_counts2):
        #     num_counts,num_counts2 = num_counts2,num_counts
        # for w in num_counts:
        #     if w not in num_counts2 or num_counts2[w] != num_counts[w]:
        #         print(num_counts,num_counts2)
        #         return False
        # return True

        #method 2
        char = [0] *26
        for i in s:
            char[ord(i) - ord('a')] +=1 # turn char into a fix number 
        for j in t:
            char[ord(j) - ord('a')] -=1
        for i in char:
            if i !=0:
                return False
        return True