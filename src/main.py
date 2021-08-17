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
            if r:
                f.write(f"{r[0]}: {r[1]}\n")
            else:
                f.write("\n")


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

    binary_original = ascii_string_to_binary(message)
    original_num_bits = len(binary_original)

    frequency = character_frequency(path)
    ht = HuffmanTree(frequency)

    binary_huffman, table = ht.encode(message)
    new_num_bits = len(binary_huffman)
    num_bits_in_table = len("".join(v[1] for v in table.values()))
    print(num_bits_in_table)
    table_size = (len(table)*8) + num_bits_in_table
    total_bit_size = table_size + new_num_bits

    compression_ratio = total_bit_size / original_num_bits

    # to make the output file easier to read, `None` will be used to
    # write new line characters
    results = [
        ("original message", message),
        ("message in binary", binary_original),
        ("message bit size", original_num_bits),
        None,
        ("message in binary using huffman coding", binary_huffman),
        ("new bit size", new_num_bits),
        ("table size", table_size),
        ("total size", total_bit_size),
        None,
        ("compression results", f"{compression_ratio:0.2%} compression")
    ]

    create_results_file(results)


if __name__ == "__main__":
    main()
