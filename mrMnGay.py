import heapq

def Dijkstra(G, s):
    V = []
    # 建立一个存储当前所有顶点信息的字典,用于实时更新
    status = {}
    for i in G:
        Adj = []
        for j in G[i]:
            Adj.append(j)
        if i != s:
            status[i] = {'dis': 10000, 'path': None, 'adj': Adj}
        else:  # 顶点s作为起点
            status[i] = {'dis': 0, 'path': 0, 'adj': Adj}
        V.append((status[i]['dis'], i))


    known = []  # 已确定路径上的顶点列表
    num = len(V)  # 顶点总数
    heap = []
    for n in V:
        heapq.heappush(heap, n)
    while len(known) != num:
        minDis = heapq.heappop(heap)
        print(minDis)
        #dis = minDis[0]
        item = minDis[1]
        if item in known:
            continue
        else:
            known.append(item)
            for n in status[item]['adj']:
                if status[n]['dis'] > status[item]['dis'] + G[item][n]:
                    status[n]['dis'] = status[item]['dis'] + G[item][n]
                    status[n]['path'] = item
                    temp = (status[n]['dis'], n)
                    heapq.heappush(heap, temp)
    print(status)




G = {'A': {'B': 1, 'C': 5}, 'B': {'D': 3}, 'C': {'D': 9}, 'D': {'A': 12}}

Dijkstra(G, 'A')