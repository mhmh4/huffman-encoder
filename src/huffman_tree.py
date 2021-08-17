import heapq

from node import Node


class HuffmanTree:

    def __init__(self, pairs: dict):
        if len(pairs) == 0:
            ...

        # sorts the dictionary by values descending
        pairs = dict(sorted(pairs.items(), key=lambda x: x[1], reverse=True))

        self._nodes = self._create_nodes(pairs)
        self.references = [x for x in self._nodes]
        print(self._nodes)
        self.root = self._build()
        a = self.get_table()
        print(a)

    def get_table(self):
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

    def _build(self) -> None:
        heapq.heapify(self._nodes)
        while len(self._nodes) > 1:
            a = heapq.heappop(self._nodes)
            b = heapq.heappop(self._nodes)
            n = Node(freq=(a.freq + b.freq))
            n.left = a
            n.right = b
            self._nodes.insert(0, n)
        return self._nodes[0]

    def _create_nodes(self, pairs: dict) -> list:
        return list(Node(k, v) for k, v in pairs.items())
