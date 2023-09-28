from queue import PriorityQueue

from breadth_first_search import graph
from iterative_deepening_search import get_neighbors


def uniform_cost_search(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        current_cost, current_node = open_set.get()

        if current_node == goal:
            return reconstruct_path(came_from, goal)

        for neighbor, cost in get_neighbors(current_node):
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                open_set.put((g_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path
