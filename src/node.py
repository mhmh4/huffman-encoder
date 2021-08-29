class Node:
    def __init__(self, 
                 char: str = None, 
                 freq: int = 0, 
                 left: "Node" = None, 
                 right: "Node" = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return f"Node({self.char=}, {self.freq=})"
