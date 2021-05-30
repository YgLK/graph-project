import numpy as np
from networkx import DiGraph

class  Edmonds_Karp:

    def __init__(self, res_graph:DiGraph):
        self.res_graph = res_graph  # create residual graph

    # Use breadth-first search in order to find augmenting paths in graph
    def bfs(self, s, t, parent):
        # Declare number of nodes in graph
        node_count = self.res_graph.number_of_nodes()
        # Declare 'visited' array - at the beginning consisting of zeros: 0 - unvisited node, 1 - visited node
        visited = np.zeros(node_count)
        # Mark source node as visited
        visited[s] = 1
        # Declare queue which contain nodes to consider in the path
        queue = []
        queue.append(s)
        # Find path from source to destination
        while len(queue) != 0:
            u = queue.pop(0)
            for i in self.res_graph.successors(u):
                # When 'i' (successor of u) vertice is not visited add it into the queue, mark as visited and
                # mark its parent as u (u becomes its previous vertice in the path - predecessor)
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
                    parent[i] = u
        # Return True if there is path between source and destination
        return bool(visited[t])

    # Solve the max_flow problem - find maximum flow from source to destination
    def solve(self, source, destination):
        # Declare array which contains information about vertices along the path
        parent = [-1] * self.res_graph.number_of_nodes()
        max_flow = 0
        # Do until no augmenting path found
        while self.bfs(source,destination,parent):
            current_path_flow = np.Inf
            v = destination
            # Find minimal residual capacity along the path
            while v != source:
                current_path_flow = min(current_path_flow, self.res_graph[parent[v]][v]["weight"])
                v = parent[v]
            # Add flow of the current found path to the actual maximum flow
            max_flow += current_path_flow
            v = destination
            # Do until source and destination meet
            while v != source:
                u = parent[v]
                # Update residual graph edge capacities
                self.res_graph[u][v]["weight"] -= current_path_flow
                if self.res_graph[u][v]["weight"] <= 0:
                    self.res_graph.remove_edge(u,v)
                if (v,u) in self.res_graph.edges():
                    self.res_graph[v][u]["weight"] += current_path_flow
                else:
                    self.res_graph.add_edge(v,u, weight=current_path_flow)
                v = u
        return max_flow