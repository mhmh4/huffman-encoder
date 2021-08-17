import collections
import os
import sys

from huffman_tree import HuffmanTree


def character_frequency(file_path: str) -> dict:
    c = collections.Counter()
    with open(file_path, "r") as f:
        for line in f:
            c += collections.Counter(line)
    return c


def ascii_string_to_binary(s: str) -> str:
    result = ""
    for char in s:
        result += bin(ord(char))[2:].zfill(8)
    return result


def create_results_file(results: list) -> None:
    with open("output/results.txt", "w") as f:
        for r in results:
            f.write(f"{r[0]}: {r[1]}\n")


def main():
    if len(sys.argv) < 2:
        print("Error: specify a file path")
        sys.exit(1)
    else:
        path = sys.argv[1]

    if not os.path.exists(path):
        print(f"Error: no such file '{path}'", file=sys.stderr)
        sys.exit(1)

    with open(path, "r") as f:
        message = f.read()

    frequency = character_frequency(path)
    ht = HuffmanTree(frequency)
    # print(f"{message}", type(message))
    binary = ascii_string_to_binary(message)
    binary_huffman = ht.encode(message)

    results = [
        ("original message", message),
        ("message in binary", binary),
        ("message bit size", len(binary)),
        ("message byte size", len(binary) // 8),
        ("message in binary using huffman coding", binary_huffman)
    ]

    create_results_file(results)



if __name__ == "__main__":
    main()
