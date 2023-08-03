class Graph:
    def __init__(self, value):
        self.value = value
        self.destinations = []

    def add_destination(self, destination_node):
        self.destinations.append(destination_node)
        destination_node.destinations.append(self)

    def find_all_paths(self, start, finish, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == finish:
            return [path]

        paths = []
        for node in start.destinations:
            if node not in path:
                found_paths = self.find_all_paths(node, finish, path)
                for found_path in found_paths:
                    paths.append(found_path)

        return paths

N = 5 # banyak perempatan di kota Surabaya
M = 2 # usia Roronoa Zoro

# Create a sample graph
graph_0 = Graph("0")
graph_1 = Graph("1")
graph_2 = Graph("2")
graph_3 = Graph("3")
graph_4 = Graph("4")

graph = [graph_0, graph_1, graph_2, graph_3, graph_4]

graph_0.add_destination(graph_1)
graph_0.add_destination(graph_4)
graph_1.add_destination(graph_2)
graph_1.add_destination(graph_3)
graph_1.add_destination(graph_4)
graph_2.add_destination(graph_3)
graph_3.add_destination(graph_4)

print("Persimpangan yang harus dihindari: ")
for i in range(N):
  if len(graph[i].destinations) > M:
    print(f"Persimpangan {graph[i].value}")
    
