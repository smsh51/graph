# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:06:21 2022

@author: Hazavei
"""


# %% graph
class Graph:
    """all problem in graph"""
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
            self.graph.setdefault(start, []).append({end: weight})
            self.node.add(end)
            self.node.add(start)
        else:
            raise Exception('can not add NoneType edg')

    def add_node(self, node: str):
        if node is not None:
            self.graph.setdefault(node, [])
            self.node.add(node)
        else:
            raise Exception('can not add NoneType node')

    def remove_node(self, node):
        if node is not None:
            try:
                self.graph.pop(node)
                self.node.remove(node)
            except:
                raise Exception('node not found')
        else:
            raise Exception('can not remove NoneType')

    def remove_edg(self, start: str, end: str, weight: int):
        if (start is not None) and (end is not None):
            try:
                self.graph[start].remove({end, weight})
            except:
                raise Exception('start or end node not found')
        else:
            raise Exception('can not remove NoneType')

    def deg(self, node):
        return len(self.graph[node])

    def isolated(self):
        node_name = []
        for i in self.graph:
            if len(self.graph[i]) == 0:
                node_name.append(i)
        return node_name

    def is_isolated(self, node):
        return self.deg(node) == 0


# %% code
self = Graph()
self.add_edg(start='A', end='c')
self.add_edg('A', 'b')
self.add_edg('b', 'c')
self.add_edg('b', 'd')
self.add_edg('d', 'c')

print(self)
