# 计算每一个domins以及它的sub domains的累计访问量
def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        1) defaultdict的初始化需要把int放在里面,不然的话后面进行第一次累加的情况会报错,因为key的value是空的不为0 2)不是每一个domain都是由三个subdomians组成的,所以要分情况讨论不然会出错
        """
        # create a defaultDict to handle the initiation
        counts = defaultdict(int)
        res = []
        # traverse over each domains
        for i in cpdomains:
            # calculate the counts for that domain
            visit = int(i.split(' ')[0].strip())
            print(visit)
            # find the partent domain
            parentDomain = i.split(' ')[1]
            # check if the domain consist with two parts or more than two parts
            domains = parentDomain.split('.')
            # construct the sub domains accordingly
            if len(domains) >=3:
                domain1 = '.'.join(domains[1:])
                domain2 = domains[-1]
                counts[parentDomain] += visit
                counts[domain1] += visit
                counts[domain2] += visit
            else: 
                domain2 = domains[-1]
                counts[parentDomain] += visit
                counts[domain2] += visit
        # traverse over the dict to create the string based on the requirement 
        for k,v in counts.items():
            res.append(str(v) + ' ' + str(k))
        return res
