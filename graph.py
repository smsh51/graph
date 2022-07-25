# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:06:21 2022

@author: Hazavei
"""
#%% graph
class Graph:
    """all ploblem in graph"""
    def __init__(self):
        self.graph = {}
        
    def add_edg(self, start:str, end:str, weight:int=0):
        self.graph.setdefault(start, []).append({end:weight})
        
        
#%% code
self = Graph()
self.add_edg('A', 'c')

self.graph
