# Dijkstra algorithm
def dijkstra(n, u): # n is the graph, u is the origin npde
    # bigV is the set of nodes
    bigV = list(n.keys()) 
    # cV is the current choices
    cV = {} 
    for a in bigV:
        cV[a] = float('inf')
    cV[u] = 0
    bigS = {u: 0}
    while bigV != None:
        i = n[u]
        for dic in i:
            ep = list(dic.keys())[0]
            if cV[ep] == None:
                continue
            elif dic[ep] + cV[u] < cV[ep]:
                cV[ep] = dic[ep] + cV[u]
        cV[u] = None
        minP = minValue(cV)
        bigV.remove(u)
        u = minP
        bigS[u] = cV[minP]
    return bigS


def minValue(a):  # find the min in a dic's values
    # todo: how to put key-value pairs into heap to sort ?
    minv = 0
    for i in list(a.values()):
        if i != None:
            minv = i
            break
    minp = ''
    for k in a.keys():
        if a[k] == None:
            continue
        if a[k] <= minv:
            minv = a[k]
            minp = k
    return minp


a = {
    't': [{'r': 2}, {'s': 9}],
    'r': [{'t': 2}, {'s': 6}, {'q': 3}],
    'q': [{'r': 3}, {'s': 2}, {'p': 4}],
    's': [{'t': 9}, {'r': 6}, {'q': 2}, {'p': 7}],
    'p': [{'q': 4}, {'s': 7}]
}
originNode = 't'
print(dijkstra(a,originNode))
