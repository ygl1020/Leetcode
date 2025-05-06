#给你一个二维数组,二维数组存储了from airpot to airpot,然后让你根据lexical的顺序来找到出发点为jfk到最后一个节点的路径
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        方法1是用的回溯,但是超时了.方法2用的dfs,没有用回溯.可以这样写的原因是因为题目说了如果我们准从lexical order并且把所有ticket都用了一遍的话就保证至少有一个解.因此在一开始我们先把ticket进行排序,
        然后创建一个adj的字典用来储存从sur出发能到达的所有outgoing的点. 然后我们开始递归,递归的条件是当src再dict里面,并len(src)>0-->这代表ticket还没有被遍历完需要继续下去,如果遍历到了最后一个
        节点的话,adj[src]会不存在然后退出循环.这时的结果从最后一个节点开始append,一直到最开始的jfk,因此我们需要把res进行反转.另外要注意的是我们每次更新下一个node是取adj[src][0]-->因为我们需要
        准从lexical order才能保证找到答案,另外记住一定要删除adj里面遍历过的点,否者就错了
        """
        # createa dict to store the src and its outgoing nodes
        # tickets.sort()
        # adj = {src:[] for src,v in tickets}
        # for k,v in tickets:
        #     adj[k].append(v)
        # res = ['JFK']
        # def backtracking(src):
        #     if len(res) == len(tickets)+1:
        #         return True
        #     tmp = list(adj[src])
        #     for i,v in enumerate(tmp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if backtracking(v):
        #             return True
        #         adj[src].insert(i,v)
        #         res.pop()
        #     return False
        # backtracking("JFK")
        # return res
        #method2
        """
        这题根据题目的提示因为如果按照lexcical的顺序一定有答案,并且要把所有的ticket用完并且每一张ticket只用一次.所以我们可以根据这个提示使用欧拉路径算法.欧拉路径
        一般使用后序遍历,因为使用前序的话我们再一开始就把node放入res数组,但是我们并不能确定这个顺序会不会遇见死胡同.所以我们需要使用后序遍历再找到路径之后开始把结果
        放入res数组.这时放入的顺序是从路径后到前的因此最好需要把res进行反转
        """
        tickets.sort()
        adj = {k:[] for k,v in tickets}
        for k,v in tickets:
            adj[k].append(v)
        res = []
        print(adj)
        def dfs(depart):
            while depart in adj and len(adj[depart])>0:
                print(res)
                to = adj[depart][0]
                # res.append(to)
                adj[depart].pop(0)
                dfs(to)
            res.append(depart)
        dfs('JFK')
        # return res
        return res[::-1]
    
    
board = ['.'*4] *4
print(board)