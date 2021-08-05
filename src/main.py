from collections import Counter
from sys import argv, exit

from huffman_tree import HuffmanTree
from node import Node


def get_character_frequency(file) -> dict:
    c = Counter()
    with open(file, "r") as f:
        for line in f:
            c += Counter(line)
    return c


def main():
    if len(argv) < 2:
        print("Error: specify a file path to be encoded")
        exit(1)
    path = argv[1]
    freq = get_character_frequency(path)
    print(freq)

# with open("output", "w") as f:
#     ...

# d = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))


# nodes = []

# for k, v in c.items():
#     x = Node(k, v)
#     nodes.append(x)

# def f():
#     a = nodes.pop()
#     b = nodes.pop()
#     total = a.freq + b.freq
#     x = Node(freq=total, left=a, right=b)
#     nodes.insert(0, x)

# i = len(nodes)
# while i != 0:
#     f()
#     i //= 2

# for x in nodes:
#     print(x)

# root = nodes[0]


# def inorder(root):
#     if not root:
#         return
#     inorder(root.left)
#     print(root.char, root.freq)
#     inorder(root.right)

# inorder(root)

if __name__ == "__main__":
    main()
