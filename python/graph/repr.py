"""
This module contains functions for representing a graph in
a more graphical form.
"""

import matplotlib.pyplot as plt # type: ignore
from . import Graph

def display(graph: Graph) -> None:
    plt.figure()
    for node_id, node in graph.nodes.items():
        plt.scatter(node.x, node.y, label=f"Node {node_id}")
        for edge in graph.edges[node_id]:
            plt.plot([node.x, edge.node2.x], [node.y, edge.node2.y], "k-", lw=0.5)
            
    plt.legend()
    plt.show()
        
    return