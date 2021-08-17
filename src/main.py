from collections import Counter
from sys import argv, exit

from huffman_tree import HuffmanTree


def character_frequency(file_path: str) -> dict:
    c = Counter()
    with open(file_path, "r") as f:
        for line in f:
            c += Counter(line)
    return c


def ascii_string_to_binary(s: str) -> str:
    result = ""
    for char in s:
        result += (bin(ord(char))[2:]).zfill(8)
    return result


def main():
    # if len(argv) < 2:
    #     print("Error: specify a file path")
    #     exit(1)
    # path = argv[1]

    f = open("src/input.txt")
    path = "src/input.txt"
    freq = character_frequency(path)
    ht = HuffmanTree(freq)
    text = f.read()
    a = ht.encode(text)
    print(a)
    b = ascii_string_to_binary(text)
    print(b)
    print(len(b))

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
