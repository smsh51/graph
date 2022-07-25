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

    def __str__(self):
        return str(list(self.graph))

    def __len__(self):
        return self.graph.__len__()

    def add_edg(self, start: str, end: str, weight: int = 0):
        self.graph.setdefault(start, []).append({}.setdefault(end, weight))


# %% code
self = Graph()
self.add_edg('A', 'c')
self.add_edg('A', 'b')
self.add_edg('b', 'c')
self.add_edg('b', 'd')
self.add_edg('d', 'c')

print(self)
