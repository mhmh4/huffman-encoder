from node import Node


class HuffmanTree:
    """"""

    def __init__(self, pairs):
        self._sort_dict_by_values_desc(pairs)
        nodes = self._create_nodes(pairs)
        root = nodes[0]
        print(root)

    def _sort_dict_by_values_desc(d: dict) -> None:
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    def _create_nodes(self, pairs: dict) -> list:
        nodes = []
        for k, v in pairs.items():
            n = Node(k, v)
            nodes.append(n)
        return nodes
