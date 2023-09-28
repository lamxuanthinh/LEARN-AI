def depth_limited_search(node, goal, depth_limit):
    if node == goal:
        return [node]
    if depth_limit == 0:
        return []

    for neighbor in get_neighbors(node):
        result = depth_limited_search(neighbor, goal, depth_limit - 1)
        if result:
            return [node] + result
    return []


def iterative_deepening_search(start, goal):
    depth_limit = 0
    while True:
        result = depth_limited_search(start, goal, depth_limit)
        if result:
            return result
        depth_limit += 1


def get_neighbors(node):
    return []

start_node = 'A'
goal_node = 'D'

result = iterative_deepening_search(start_node, goal_node)
if result:
    print("Path from", start_node, "to", goal_node, ":", result)
else:
    print("No path found from", start_node, "to", goal_node)
