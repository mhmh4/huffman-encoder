from node import Node


class HuffmanTree:

    def __init__(self, pairs):
        self._sort_dict_by_values_desc(pairs)
        self._nodes = self._create_nodes(pairs)
        self.root = self._nodes[0]
        self.root = self._build()
        print(self.root)

    def _sort_dict_by_values_desc(self, d: dict) -> None:
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    def _build(self) -> None:
        while len(self._nodes) > 1:
            # a = self._nodes[-1].freq
            # b = self._nodes[-2].freq
            a = self._nodes.pop()
            b = self._nodes.pop()
            combined_freq = a.freq + b.freq
            n = Node(freq=combined_freq, left=a, right=b)
            self._nodes.insert(0, n)
        return self._nodes[0]

    def _create_nodes(self, pairs: dict) -> list:
        nodes = []
        for k, v in pairs.items():
            n = Node(k, v)
            nodes.append(n)
        return nodes
