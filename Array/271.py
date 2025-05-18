#写两个function来decod和encode字符串
def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
            我们把每一个字符串的长度放再起始位置,然后加一个分割符号来辅助后面decode时的切分
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' +s
        return res
        

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
        我们再字符串中先找到分隔符,然后计算当前需要decode的字符串的长度,然后把字符串放入res数组,最后更新i的下标, 这里最好不要用for循环,因为for循环是一定会比
        遍历每一个元素,但是如果出现字符串本身就是'#'的情况可能提length时就会出错:'1##', 在提取完#后我们的for循环会继续遍历下去
                """
    print(s)
    res = []
    i = 0
    # for r in range(0,len(s)):  
    #     if s[r] == '#':
    #         length = int(s[l:r])
    #         res.append(s[r+1:r+length+1])
    #         l = r+1+length
    while i <len(s):
        j = i
        while s[j] != '#':
            j +=1
        length = int(s[i:j])
        res.append(s[j+1:j+length+1])
        i = j+1+length
    print(res)
    return res