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
    # if len(argv) < 2:
    #     print("Error: specify a file path to be encoded")
    #     exit(1)
    # path = argv[1]
    path = "src/input.txt"
    freq = get_file_char_freq(path)
    ht = HuffmanTree(freq)
    # print(ht)
    # print(ht.root.left)

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


if __name__ == "__main__":
    main()
