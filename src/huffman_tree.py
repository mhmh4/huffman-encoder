import heapq

from node import Node


class HuffmanTree:

    def __init__(self, pairs: dict):
        self.nodes = self._create_nodes(pairs)
        self.root = self._build_tree()
        self.table = self._build_table()

    def _create_nodes(self, pairs: dict) -> list:
        return list(Node(k, v) for k, v in pairs.items())

    def _build_tree(self) -> Node:
        heapq.heapify(self.nodes)
        while len(self.nodes) > 1:
            smallest_1 = heapq.heappop(self.nodes)
            smallest_2 = heapq.heappop(self.nodes)
            total_freq = smallest_1.freq + smallest_2.freq
            n = Node(freq=total_freq, left=smallest_1, right=smallest_2)
            heapq.heappush(self.nodes, n)
        return self.nodes[0]

    def _build_table(self) -> dict:
        result = {}
        def traverse(node, path=""):
            if node:
                traverse(node.left, path=(path + "0"))
                if node.char:
                    result[node.char] = path
                traverse(node.right, path=(path + "1"))
            return result
        traverse(self.root)
        return result
