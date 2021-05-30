import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
nx.graphviz_layout = graphviz_layout
from algorithm.main_algo import Edmonds_Karp

# Read graph from file
filename = 'graph.json'     # Change filename in order to run algorithm on different graph e.g. filename = 'graph_template.json'
f = open(filename)          # Remember to change name of the generated visualisation of the graph - line 37 - as well
vertices, edges, ends = json.loads(f.read())

verCount = len(vertices)
C = np.zeros((verCount, verCount))

# Generate adjacency matrix for the graph
for i in range(verCount):
    for j in range(verCount):
        for k in range(len(edges)):
            if edges[k][0] == i and  edges[k][1] == j:
                C[i][j] = edges[k][2]
            elif edges[k][0] == j and  edges[k][1] == i:
                C[j][i] = edges[k][2]

print("Adjacency matrix:")
print(C)
G = nx.from_numpy_matrix(C, create_using=nx.DiGraph)

# Create visualization (drawing.png) of the graph
pos=nx.graphviz_layout(G, prog="neato")
plt.figure(figsize=(7, 7))
nx.draw_networkx(G, pos)
plt.draw()
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("graph.png")                      # Enter the name of graph picture  e.g. plt.savefig("graph_template.png")
plt.close()

# Add necessary attributes in order to run maximum_flow_value on graph G
capacities = {(u,v):G[u][v]["weight"] for u,v in G.edges()}
nx.set_edge_attributes(G, capacities, 'capacity')

# Declaration of SOURCE and DESTINATION in the graph
source = ends[0]
destination = ends[1]

# Check if max_flow result from built-in networkx library function 'nx.maximum_flow_value'
# is equal to the result of implemented Edmonds-Karp algorithm
f = Edmonds_Karp(nx.from_numpy_matrix(C, create_using=nx.DiGraph))
print("Correct max flow: " + str(nx.maximum_flow_value(G,source,destination)))
print("Edmonds-Karp algorithm max flow:  "  +  str(f.solve(source = source, destination= destination)))