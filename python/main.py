import json
from graph import Node, Edge, Graph
from graph.repr import display
from collections.abc import Hashable

Number = float | int

def read_json(PATH:str) -> dict:
    json_dict = {}
    with open(PATH, "r") as file:
        json_dict = json.load(file)
        
    return json_dict

def convert_to_node(nodes:list[dict[Hashable, str, Number, Number]]) -> list[Node]:
    new_nodes = []
    for node in nodes:
        new_nodes.append(Node(node["id"], node["x"], node["y"]))
    return new_nodes

def find_node(node_id:Hashable, nodes:list[Node]) -> Node | None:
    for node in nodes:
        if node_id == node.id:
            return node
    return None
        
def convert_to_edge(edges:list[dict[Hashable, Hashable, Number]], nodes:list[Node]):
    new_edges = []
    for edge in edges:
        node1 = find_node(edge["node1"], nodes)
        node2 = find_node(edge["node2"], nodes)
        cost = edge["distance"]
        new_edges.append(Edge(node1, node2, cost))
    return new_edges
        

def main() -> None:
    graph_repr = read_json("settings.json")
    nodes = convert_to_node(graph_repr["nodes"])
    edges = convert_to_edge(graph_repr["edges"], nodes)
    graph = Graph(nodes=nodes, edges=edges)
    print(graph.nodes)
    print(graph.edges)
    display(graph)
    return

if __name__ == '__main__':
    main()