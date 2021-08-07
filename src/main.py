from collections import Counter
from sys import argv, exit

from huffman_tree import HuffmanTree


def get_file_char_freq(file) -> dict:
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
    freq = get_file_char_freq(path)
    ht = HuffmanTree(freq)
    print(ht)
    print(ht.root.left)

    # data = []
    # with open("src/input.txt", "r") as f:
    #     for line in f:
    #         for char in line:
    #             data.append(char)
    # byte_string = ""
    # for x in data:
    #     ascii_code = ord(x)
    #     bin_ = bin(ascii_code)[2:]
    #     hex_ = hex(ascii_code)
    #     formatted = hex_[2:].zfill(8)
    #     print(
    #         x,
    #         bin_,
    #         hex_,
    #         #formatted,
    #         end=" ")
    #     for i in range(0, 32, 4):
    #         byte = formatted[i:i+5]
    #         print(byte, end=" ")
    #     print()
    # with open("output.txt", "w") as f:
    #     f.write("hello\n")



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
