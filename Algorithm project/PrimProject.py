import heapq
mst = []
usedVertices = set()
numVertices = int(input('How many Shops? '))
edges = [[] for j in range(numVertices+1)]
data = input('enter data:')
lines = data.split(' ')
for i in range(0,len(lines),3):
    tmp = lines[i:i+3]
    edge = tuple (map(int, tmp))
    if edge[0] == edge[1]:continue
    heapq.heappush(edges[edge[0]], (edge[2], edge[1]))
    heapq.heappush(edges[edge[1]], (edge[2], edge[0]))
cost, dest= 0, 1
while len(usedVertices)< numVertices:
    vertexWithSmallestEdge = 0
    for vertex in usedVertices:
        while len(edges [vertex]) > 0 and edges [vertex][0][dest] in usedVertices:
            heapq.heappop (edges [vertex])
        if len(edges[vertex]) == 0: continue
        if len(edges[vertexWithSmallestEdge]) == 0 or edges[vertex][0][cost]< edges [vertexWithSmallestEdge][0][cost]:
            vertexWithSmallestEdge = vertex
    edge = heapq.heappop(edges[vertexWithSmallestEdge])
    mst.append((vertexWithSmallestEdge, edge[dest], edge[cost]))
    usedVertices.add(vertexWithSmallestEdge)
    usedVertices.add(edge[dest])
print(mst)