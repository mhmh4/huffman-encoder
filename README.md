# Huffman Encoder

## Introduction

Huffman coding is an algorithm that's used for lossless text compression. In a nutshell, Huffman coding does its compression by storing the least amount of space for the most frequent characters. A good visualization of how the algorithm works can be seen by [Tom Scott's video on text compression](https://www.youtube.com/watch?v=JsTptu56GM8).

This program uses that technique to show how much data can be saved for a particular message that the user will input. It may not always be the case that the algorithm will save more space than the original amount since it needs to store additional information apart from the encoded message.

<div align="center">
  <img width="40%" src="assets/diagram.svg">
  <p>The Huffman tree for the message, 'BCCABBDDAECCBBAEDDCC'</p>
</div>

## Requirements

- Python 3.9

## Getting started

#### Download the repository using Git or download the zip file.
```bash
$ git clone https://github.com/u06/huffman-encoder.git
```

#### `cd` into it.

```
$ cd huffman-encoder
```

#### Within the `input` directory, enter some text within `message.txt`.

```bash
$ echo -n 'BCCABBDDAECCBBAEDDCC' > message.txt
```

#### From the repository's root, run `main.py` specifying `message.txt`'s path

```bash
$ python3 src/main.py input/message.txt
```

#### Within the `output` directory, there will be a `results.txt` file that contains the results of Huffman coding used on `message.txt`'s contents.

```
$ cat output/results.txt
ASCII
---
message: BCCABBDDAECCBBAEDDCC
message (binary): 0100001001000011010000110100000101000010010000100100010001000100010000010100010101000011010000110100001001000010010000010100010101000100010001000100001101000011
bit size: 160

Huffman coding
---
message (binary): 011111101010100001011001111010110110000001111
bit size: 45
table size: 52
total size: 97

result: 60.62% compression
```
