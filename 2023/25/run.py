import igraph as ig

graph = ig.Graph()
with open("input.txt") as file:
    for line in file:
        entry_node, raw_dests = line.strip().split(":")
        dest_nodes = raw_dests.strip().split(" ")
        for dest_node in dest_nodes:

            try :
                graph.vs.find(name=entry_node)
            except:
                graph.add_vertex(entry_node)

            try :
                graph.vs.find(name=dest_node)
            except:
                graph.add_vertex(dest_node)
            graph.add_edge(entry_node, dest_node)

len_part = 1
for part in graph.mincut().partition:
    len_part *= len(part)
    print(len_part)
