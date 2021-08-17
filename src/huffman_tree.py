import heapq

from node import Node


class HuffmanTree:

    def __init__(self, frequency: dict[str, int]):
        self._nodes = self._create_nodes(frequency)
        self._root = self._build_tree()
        self.table = self._build_table()

    def encode(self, message: str) -> tuple[str, dict]:
        result = ""
        for char in message:
            code = self.table[char][1]
            result += code
        return (result, self.table)

    def _create_nodes(self, frequency: dict[str, int]) -> list:
        return list(Node(k, v) for k, v in frequency.items())

    def _build_tree(self) -> Node:
        heapq.heapify(self._nodes)
        while len(self._nodes) > 1:
            smallest_1 = heapq.heappop(self._nodes)
            smallest_2 = heapq.heappop(self._nodes)
            total_freq = smallest_1.freq + smallest_2.freq
            n = Node(freq=total_freq, left=smallest_1, right=smallest_2)
            heapq.heappush(self._nodes, n)
        return self._nodes[0]

    def _build_table(self) -> dict:
        result = {}
        def traverse(node, path=""):
            if node:
                traverse(node.left, path=(path + "0"))
                if node.char:
                    result[node.char] = (node.freq, path)
                traverse(node.right, path=(path + "1"))
            return result
        traverse(self._root)
        return result
