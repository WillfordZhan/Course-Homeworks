import heapq
def dijkstra(n,u):
    # bigV is the set of nodes
    bigV = list(n.keys())
    bigS = {u: 0}
    # cV is the current choices
    cV = []
    for a in bigV:
        if a == u:
            cV.append((a,0))
        else:
            cV.append((float('inf'), a))
    
    heap = []
    for i in cV:
        heapq.heappush(heap, i)
    known = []
    while len(bigV) != 1:
        selectedt = heapq.heappop(heap)
        u = selectedt[1]
        i = n[u]
        for dic in i:
            ep = list(dic.keys())[0]
            for t in cV:
                if t[1] in known:
                    continue
                else dic[ep] + cV[u] < t[0]:
                    t[0] = dic[ep] + cV[u]
                    temp = (t[0], ep)
                    heapq.heappush(heap, temp)
        known.append(u)
        bigV.remove(u)
        bigS[u] = cV[minP]
    return bigS
