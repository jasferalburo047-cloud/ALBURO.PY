"""
Assessment 3.3: Non-linear Data Structure
Surname: ALBURO  ->  nodes: A, L, B, U, R, O
"""
from collections import deque


# ---------- Diagram 1: Binary Tree ----------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    #        A
    #       / \
    #      L   B
    #     / \   \
    #    U   R   O
    root = Node("A")
    root.left = Node("L")
    root.right = Node("B")
    root.left.left = Node("U")
    root.left.right = Node("R")
    root.right.right = Node("O")
    return root


# ---------- Diagram 2: Graph ----------
def build_graph():
    edges = [("A", "L"), ("A", "B"), ("L", "U"),
             ("B", "R"), ("U", "O"), ("R", "O")]
    graph = {v: [] for v in "ALBURO"}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    return graph


# ---------- Diagram 3: Linear traversal ----------
def traverse_left_to_right(arr):
    result = []
    i = 0
    while i < len(arr):
        result.append(arr[i])
        i += 1
    return result


def traverse_right_to_left(arr):
    result = []
    i = len(arr) - 1
    while i >= 0:
        result.append(arr[i])
        i -= 1
    return result


# ---------- Diagram 4: Linear search ----------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------- Diagram 5: BFS on tree ----------
def bfs_tree(root):
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ---------- Diagram 6: DFS on tree (preorder) ----------
def dfs_tree(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)
    dfs_tree(node.left, result)
    dfs_tree(node.right, result)
    return result


# ---------- Diagram 7: BFS on graph ----------
def bfs_graph(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return result


# ---------- Diagram 8: DFS on graph ----------
def dfs_graph(graph, vertex, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(vertex)
    result.append(vertex)
    for n in graph[vertex]:
        if n not in visited:
            dfs_graph(graph, n, visited, result)
    return result


if __name__ == "__main__":
    arr = ["A", "L", "B", "U", "R", "O"]
    tree = build_tree()
    graph = build_graph()

    print("Graph adjacency list:", graph)
    print("Linear  Left->Right :", " - ".join(traverse_left_to_right(arr)))
    print("Linear  Right->Left :", " - ".join(traverse_right_to_left(arr)))
    print("Search 'U' index    :", linear_search(arr, "U"))
    print("Search 'Z' index    :", linear_search(arr, "Z"))
    print("Tree  BFS           :", " - ".join(bfs_tree(tree)))
    print("Tree  DFS           :", " - ".join(dfs_tree(tree)))
    print("Graph BFS           :", " - ".join(bfs_graph(graph, "A")))
    print("Graph DFS           :", " - ".join(dfs_graph(graph, "A")))