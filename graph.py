# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:06:21 2022

@author: Hazavei
"""


# %% graph
class Graph:
    """all ploblem in graph"""
    def __init__(self):
        self.graph = {}
        self.node = set()

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

    def add_edg(self, start: str, end: str, weight: int = 0):
        """
        add edg to graph
        """
        self.graph.setdefault(start, []).append({end: weight})
        self.node.add(end)
        self.node.add(start)

    def deg(self, node):
        return len(self.graph[node])


# %% code
self = Graph()
self.add_edg(start='A', end='c')
self.add_edg('A', 'b')
self.add_edg('b', 'c')
self.add_edg('b', 'd')
self.add_edg('d', 'c')

print(self)
