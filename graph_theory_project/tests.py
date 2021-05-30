import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
nx.graphviz_layout = graphviz_layout
from algorithm.main_algo import Edmonds_Karp
import random


# Randomized  tests for algorithm
number_of_tests = 10
for i in range(number_of_tests):
    # Randomize number of vertices in graph
    n = random.randint(5,10)
    # Randomize adjacency matrix (directions and weights of edges)
    C = np.random.randint(20,size=(n,n))

    # Create graph objects
    G = nx.from_numpy_matrix(C, create_using=nx.DiGraph)
    f = Edmonds_Karp(nx.from_numpy_matrix(C, create_using=nx.DiGraph))

    # Add necessary attributes in order to run maximum_flow_value on graph G
    capacities = {(u,v):G[u][v]["weight"] for u,v in G.edges()}
    nx.set_edge_attributes(G, capacities, 'capacity')

    # Declare list of all vertices in graph
    nodes_left = list(range(n))
    # Randomly pick  source
    source = random.randint(0,len(nodes_left)-1)
    # Pop source vertice form list of vertices
    nodes_left.pop(source)
    # Randomly pick  destination
    destination = random.randint(0,len(nodes_left)-1)
    destination = nodes_left[destination]

    # Calculate values of maximum flow
    correct_value = nx.maximum_flow_value(G,source,destination)
    test_value = f.solve(source = source, destination= destination)
    # Verify whether algorithm works correctly (whether results are equal)
    if correct_value == test_value:
        pass
    else:
        print("Test {number} failed".format(number=i) +
              C +
              "Correct value:"+ str(correct_value) +
              "Test value:" + str(test_value))
        exit(1)
    print("Test {number} correct value:".format(number=i) + str(correct_value))
    print("Test {number} test value:".format(number=i) + str(test_value))
print("Tests passed successfully.")