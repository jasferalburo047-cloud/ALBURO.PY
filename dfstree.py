import sys

NAME = "JASFER ALBURO"


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_tree(name):
    letters = [c.upper() for c in name if c.isalpha()]
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0] if nodes else None


def print_tree(root, gap=4):

    if root is None:
        return

    cols, depth_of, counter = {}, {}, [0]

    def assign(node, depth):
        # column of a node = its inorder position, so nothing overlaps
        if node is None:
            return
        assign(node.left, depth + 1)
        cols[node] = counter[0] * gap
        depth_of[node] = depth
        counter[0] += 1
        assign(node.right, depth + 1)

    assign(root, 0)
    height = max(depth_of.values()) + 1
    width = max(cols.values()) + 5
    grid = [[" "] * width for _ in range(3 * height - 2)]

    def draw(node):
        if node is None:
            return
        row = 3 * depth_of[node]
        for i, ch in enumerate(node.key):
            grid[row][cols[node] + i] = ch
        kids = [k for k in (node.left, node.right) if k]
        if kids:
            grid[row + 1][cols[node]] = "|"
            span = [cols[k] for k in kids] + [cols[node]]
            for c in range(min(span), max(span) + 1):
                grid[row + 2][c] = "-"
            for c in span:
                grid[row + 2][c] = "+"
        draw(node.left)
        draw(node.right)

    draw(root)
    for line in grid:
        print("".join(line).rstrip())


def print_levels(root):
    level, current = 0, [root] if root else []
    while current:
        print(f"  Level {level}: {' '.join(n.key for n in current)}")
        current = [c for n in current for c in (n.left, n.right) if c]
        level += 1




def preorder_recursive(node, out=None):

    if out is None:
        out = []
    if node:
        out.append(node.key)
        preorder_recursive(node.left, out)
        preorder_recursive(node.right, out)
    return out


def inorder_recursive(node, out=None):

    if out is None:
        out = []
    if node:
        inorder_recursive(node.left, out)
        out.append(node.key)
        inorder_recursive(node.right, out)
    return out


def postorder_recursive(node, out=None):

    if out is None:
        out = []
    if node:
        postorder_recursive(node.left, out)
        postorder_recursive(node.right, out)
        out.append(node.key)
    return out



def preorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_iterative(root):
    result, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.key)
        cur = cur.right
    return result


def postorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else NAME
    if not any(c.isalpha() for c in name):
        sys.exit("Please enter a name with letters.")

    root = build_tree(name)

    print(f"\nName: {name.upper()}")
    print("\n===== BINARY TREE =====")
    print_tree(root)
    print("\nBy level:")
    print_levels(root)

    print("\n===== DFS TRAVERSALS =====")
    methods = [
        ("PreOrder ", "Root -> Left -> Right", preorder_recursive, preorder_iterative),
        ("InOrder  ", "Left -> Root -> Right", inorder_recursive, inorder_iterative),
        ("PostOrder", "Left -> Right -> Root", postorder_recursive, postorder_iterative),
    ]
    for label, pattern, rec, itr in methods:
        r, i = rec(root), itr(root)
        print(f"{label} ({pattern})")
        print(f"  Recursive: {'->'.join(r)}")
        print(f"  Iterative: {'->'.join(i)}")
        print(f"  Match: {'yes' if r == i else 'NO'}")


if __name__ == "__main__":
    main()