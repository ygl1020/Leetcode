#787
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)] 
        for i,j,p in flights:
            g[i].append((j,p))
        price = [inf] * n
        price[src] = 0
        h = [(src,0,-1)] 
        limit = k+1
        while h:
            x,cur_price,stop = heappop(h)
            # if cur_price > price[x]: # 用这种传统的dijkstra过滤条件是错的
            #     continue
            if x == dst:
                return cur_price
            if stop ==k:
                continue
        
            for y,p in g[x]:
                new_price = cur_price + p
                if new_price < price[y]:
                    price[y] = new_price
                    heappush(h,(y,new_price,stop+1))
        print(price)
        return -1
    
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # cost[s][c] = minimal cost to reach city c using s stops.
    # We only need s up to k+1 (since "at most k stops" allows k+1 edges).
    cost = [[inf]*n for _ in range(k + 2)]
    cost[0][src] = 0  # cost to reach src with 0 stops is 0

    # (current_price, current_city, stops_used)
    heap = [(0, src, 0)]
    
    while heap:
        cur_price, city, stops_used = heappop(heap)
        
        # If we reach dst, this is guaranteed the cheapest (due to min-heap)
        if city == dst:
            return cur_price
        
        # If we can still take another flight (stop)
        if stops_used < k + 1:
            for neighbor, w in graph[city]:
                new_price = cur_price + w
                # If we found a cheaper way to neighbor with (stops_used + 1) stops
                if new_price < cost[stops_used + 1][neighbor]:
                    cost[stops_used + 1][neighbor] = new_price
                    heappush(heap, (new_price, neighbor, stops_used + 1))
    
    return -1