# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:06:21 2022

@author: Hazavei
"""

__author__ = "Sayyed mohammad saeed hazavehei"
__copyright__ = "Copyright 2022, The Cogent Project"
__credits__ = ["SmS.hZ"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "atpy"
__email__ = "saeed.hazavehei@gmail.com"
__status__ = "science"


# %% graph
class Graph:
    """
    all problem in graph
    """

    def __init__(self):
        self.graph = {}
        self.node = set()

    def hi(self): ...
    def __eq__(self, other): ...
    def __add__(self, other): ...

    def __str__(self):
        message = ''
        for key in list(self.graph):
            for val in self.graph[key]:
                message += '{start}, {end} \n'.format(start=key, end=val)
        return message.translate({ord(i): None for i in "{'}"})

    def __len__(self):
        return self.graph.__len__()

    def __contains__(self, item):
        return item in self.node

    def add_edg(self, start: str, end: str, weight: int = 1):
        """
        add edg to graph
        """
        if (end is not None) and (start is not None):
            if (start == end) and (weight == 1):
                weight = 2

            self.graph.setdefault(start, []).append({end: weight})
            self.node.add(end)
            self.node.add(start)
        else:
            raise Exception('can not add NoneType edg')

    def add_node(self, node: str):
        """
        add node to graph
        """
        if node is not None:
            self.graph.setdefault(node, [])
            self.node.add(node)
        else:
            raise Exception('can not add NoneType node')

    def remove_node(self, node: str):
        """
        remove node from graph
        """
        if node is not None:
            try:
                self.graph.pop(node)
                self.node.remove(node)
            except ValueError:
                raise Exception('node not found')
        else:
            raise Exception('can not remove NoneType')

    def remove_edg(self, start: str, end: str, weight: int):
        """
        remove edg from graph
        """
        if (start is not None) and (end is not None):
            try:
                self.graph[start].remove({end, weight})
            except ValueError:
                raise Exception('start or end node not found')
        else:
            raise Exception('can not remove NoneType')

    def degree(self, node: str):
        """
        calculate node degree
        """
        return len(self.graph[node])

    def isolated(self):
        """
        calculate isolated graph
        """
        node_name = []
        for i in self.graph:
            if self.degree(i) == 0:
                node_name.append(i)
        return node_name

    def is_isolated(self, node: str) -> bool:
        """
        calculate isolated node
        """
        return self.degree(node) == 0

    def pendant(self) -> list:
        """
        pendant is a list of node whose degree is one
        """
        node_name = []
        for i in self.graph:
            if self.degree(i) == 1:
                node_name.append(i)
        return node_name

    def degree_sequence(self):
        """
        A sequence of degrees of graph nodes
        """
        node_name = []
        for i in self.graph:
            node_name.append(self.degree(i))
        return sorted(node_name, reverse=True)

    def is_regular(self):
        """
        equal total degree in graph
        """
        degree = self.degree_sequence()
        if min(degree) == max(degree):
            return degree[0]
        return False

    def quantity_edg(self):
        """
        quantity of edges
        """
        return sum(self.degree_sequence())

    def is_valid(self):
        """
        can crate graph by degree sequence
        """
        return self.quantity_edg() % 2 == 0

    def graphic_sequence(self):
        """
        create simple graph by degree sequence
        """

    # TODO : add method 2-switch


# %% code
self = Graph()
self.add_edg(start='A', end='c')
self.add_edg('A', 'b')
self.add_edg('b', 'c')
self.add_edg('b', 'd')
self.add_edg('d', 'c')

print(self)
