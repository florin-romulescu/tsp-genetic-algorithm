"""
This module contains the logic of graphs for solving
the Travelling Salesman Problem.
"""

from typing import Callable
from collections.abc import Hashable
from dataclasses import dataclass

Number = int | float

@dataclass(frozen=True)
class Node:
    """
    Represents a node of a graph that is situated in a XoY plan.
    
    Args:
        * id: it is an hashable element that makes the distinction between two nodes.
        * x: it's x coordinate on the plan.
        * y: it's y coordinate on the plan.
    """
    id:Hashable
    x:Number = .0
    y:Number = .0
    
@dataclass(frozen=True)
class Edge:
    """
    Represents an edge between two nodes.
    
    Args:
        * node1, node2: The two nodes that the edge unites.
        * cost: a cost assigned to the edge by some rule.
    """
    node1: Node
    node2: Node
    cost: Number
    
class Graph:
    def __init__(self, nodes:list[Node]=None, edges:list[Edge]=None) -> None:
        self.nodes:dict[Hashable, Node] = {} if nodes is None else {
            node.id : node
            for node in nodes
        }
        self.edges = {
            node_id : []
            for node_id in self.nodes
        }
        
        if edges is not None:
            for edge in edges:
                self.edges[edge.node1.id].append(edge)
        
    def add_node(self, node:Node):
        self.nodes[node.id] = node
        self.edges[node.id] = []
        
    def add_edge(self, edge:Edge):
        self.edges[edge.node1.id].append(edge)
        
        reverse_edge = Edge(edge.node2, edge.node1, edge.cost)
        self.edges[reverse_edge.node1.id].append(reverse_edge)