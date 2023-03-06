class Node:
    def __init__(self, ego):
        self.ego = ego
        self.connection = {}
        self.type = set()
        self.typical_instance = set()

    def activate(self):
        pass

class Defender:
    def __init__(self, ego):
        self.ego = ego

    def is_detect(self, node1, node2):
        node1.type.add(node2)
        node2.typical_instance.add(node1)

    def is_not_detect(self, node1, node2):
        node1.type.remove(node2)
        node2.typical_instance.remove(node1)

class Center:
    def __init__(self, ego):
        self.ego = ego
