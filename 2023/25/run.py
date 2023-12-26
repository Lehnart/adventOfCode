import igraph as ig

graph = ig.Graph()
with open("input.txt") as file :
    for line in file:
        entry_node, raw_dests = line.strip().split(":")
        dest_nodes = raw_dests.strip().split(" ")
        for dest_node in dest_nodes:
            graph.add_vertex(entry_node)
            graph.add_vertex(dest_node)
            graph.add_edge(entry_node, dest_node)

edge_list = graph.get_edgelist()
print(edge_list)
for i in range(0,len(edge_list)):
    for j in range(i+1, len(edge_list)):
        for k in range(j + 1, len(edge_list)):
            graph.delete_edges(i)
            graph.delete_edges(j)
            graph.delete_edges(k)
            print(graph)