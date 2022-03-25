"""
Problem: Binary tree averages
Author: Jacob Summerville
Description: Depth-first search, add total and count to a dictionary
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.left  = None
        self.right = None


def traverse(node, depth, node_map):
    if not node: return

    if depth in node_map:
        node_map[depth].append(node.value)
    else:
        node_map[depth] = [node.value]

    depth += 1
    traverse(node.left, depth, node_map)
    traverse(node.right, depth, node_map)


def calculate_averages(node_1):
    node_map = {}
    traverse(node_1, 0, node_map)
    
    averages = []
    for depth in node_map:
        depth_sum = 0
        for node in node_map[depth]:
            depth_sum += node

        averages.append(int(depth_sum / len(node_map[depth])))

    return averages


if __name__ == '__main__':
    node_1 = Node(4)
    node_2 = Node(7)
    node_3 = Node(9)
    node_4 = Node(10)
    node_5 = Node(2)
    node_6 = Node(6)
    node_7 = Node(6)
    node_8 = Node(2)

    node_7.left  = node_8
    node_5.left  = node_7
    node_2.left  = node_4
    node_2.right = node_5
    node_3.right = node_6
    node_1.left  = node_2
    node_1.right = node_3

    print(calculate_averages(node_1))