import heapq

def calculate_shortest_path(vertexList,startVertex):
    queue=[]
    startVertex.minDistance=0
    heapq.heappush(queue, startVertex)
    while len(queue)>0:
        actualVertex=heapq.heappop(queue)
        for edge in actualVertex.adjacenciesList:
            u=edge.startVertex
            v=edge.targetVertex
            newDistance=u.minDistance + edge.weight
            
            if newDistance<v.minDistance:
                v.predecessor=u
                v.minDistance=newDistance
                heapq.heappush(queue, v)

def get_shortest_path_to(targetVertex):
    curr_node=targetVertex
    while curr_node:
        print(f"{curr_node.name} - >" , end="")
        curr_node=curr_node.predecessor