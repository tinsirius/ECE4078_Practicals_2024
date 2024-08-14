import os
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

# Import dependencies and set random seed
seed_value = 5
# 1. Set `PYTHONHASHSEED` environment variable at a fixed value
os.environ['PYTHONHASHSEED'] = str(seed_value)
# 2. Set `python` built-in pseudo-random generator at a fixed value
random.seed(seed_value)
# 3. Set `numpy` pseudo-random generator at a fixed value
np.random.seed(seed_value)


def find_nearest(array, value):
	array = np.asarray(array)
	idx = (np.linalg.norm(array - value, axis=1)).argmin()
	return idx, array[idx]


class Node:
	"""
	Node class for path search
	"""

	def __init__(self, point, cost=0, parent_index=0, roadmap_index=0):
		self.x, self.y = point
		self.cost = cost
		self.parent_index = parent_index
		self.idx_roadmap = roadmap_index

	def __str__(self):
		return str(self.x) + "," + str(self.y) + "," +\
			   str(self.cost) + "," + str(self.parent_index)
	
def breadth_first_search(road_map, start, goal):

			
	idx_start, vertex_start = find_nearest(road_map.vertices, start)
	idx_goal, vertex_goal = find_nearest(road_map.vertices, goal)
			
	start_node = Node(vertex_start, cost=0.0, parent_index=-1,roadmap_index=idx_start)
	goal_node = Node(vertex_goal, cost=0.0, parent_index=-1, roadmap_index=idx_goal)
	
	queue = [start_node]
	visited_nodes = {idx_start: start_node}
	cur_idx = 0
	
	
	def reconstruct_path():
		path = [np.array([goal[0], goal[1]]), np.array([goal_node.x, goal_node.y])]
		parent_index = goal_node.parent_index
		while parent_index != -1:
			n = visited_nodes[parent_index]
			path.append(np.array([n.x, n.y]))
			parent_index = n.parent_index
		path.append(np.array([start[0], start[1]]))
		return path
		   
	while queue:
		node = queue.pop(0)
		for idx in road_map.edges[node.idx_roadmap]:
			if idx not in visited_nodes:
				v = road_map.vertices[idx, :]
				cost = node.cost + np.linalg.norm(np.array([node.x, node.y]) - v)
				
				# Create new node and mark it as visited
				new_node = Node(v, cost=cost, parent_index=node.idx_roadmap, roadmap_index=idx)
				visited_nodes[idx] = new_node
				
				# Add it to the queue
				queue.append(new_node)
				
				# Verify if new visited node is goal 
				if np.isclose(new_node.x, goal_node.x) and np.isclose(new_node.y, goal_node.y):
					goal_node.idx_roadmap = idx
					goal_node.parent_index = node.idx_roadmap
					goal_node.cost = cost
					return reconstruct_path()
				
	return False