from graph_data_structure.dikstras_algorithm import calculate_shortest_path,\
    get_shortest_path_to
from graph_data_structure.edge import Edge
from graph_data_structure.vertex import Vertex


node1=Vertex("A")
node2=Vertex("B")
node3=Vertex("C")

edge1=Edge(1,node1,node2)
edge2=Edge(1,node2,node3)
edge3=Edge(0.1,node1,node3)

node1.adjacenciesList.append(edge1)
node2.adjacenciesList.append(edge2)
node3.adjacenciesList.append(edge3)

vertexList=[node1,node2,node3]

calculate_shortest_path(vertexList, node1)
get_shortest_path_to(node3)