
"""
发挥分布式的优势

复杂关系的组合

先解决简单问题

创造的

想的方向和好奇点，只往后推一步
            多储存往后推一步的连接点

讲出来的有意思的话和故事

            连接点够多就好判断

        人的探索和好奇是没有目的性的


        事物的本质和直接关系的   持续的有大类的联系
                高概念的连接
                        大概能猜对

        触发的信号值是1 和 0.5

        双重触发的是1.5

mom is human
human is mammal
?mom mammal
"""


class Node:
    def __init__(self, ego):
        self.ego = ego
        self.connection = {}
        self.type = set()
        self.typical_instance = set()
        self.state = 0

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

    def inference(self, node1, node2):
        hub = set()
        for node in node1.type:
            node.state += 1
            hub.add(node)
        for node in node2.typical_instance:
            node.state += 1
            hub.add(node)

        res = max(hub, key=lambda x: x.state)
        if res.state > 1:
            return True
        else:
            return False


class Center:
    def __init__(self, ego):
        self.ego = ego
        self.base = {}
        self.index = 0
        self.wording = []
        self.stack = []
        self.defender = Defender('is')
    def refresh(self):
        self.index = 0
        self.wording = []
        self.stack = []

    def get_wording(self, wording):
        self.wording = wording
        self.index = 0
    def think(self):

        while(True):

            word = self.wording[self.index]

            if word == 'is':
                word = self.wording[self.index+1]
                if not word in self.base:
                    self.base[word] = Node(word)
                self.defender.is_detect(self.stack[-1], self.base[word])
                self.stack.append(self.base[word])
                return

            elif word == '?':
                node1 = self.wording[self.index+1]
                node2 = self.wording[self.index+2]

                node1 = self.base[node1]
                node2 = self.base[node2]

                res = self.defender.inference(node1, node2)
                self.refresh()
                return res

            else:
                if not word in self.base:
                    self.base[word] = Node(word)
                self.stack.append(self.base[word])
                self.index+=1



def main():
    center = Center('center')
    center.get_wording(['mom', 'is', 'human'])
    center.think()
    center.get_wording(['human', 'is', 'mammal'])
    center.think()
    center.get_wording(['?', 'mom', 'mammal'])
    res = center.think()
    print(res)

    center.get_wording(['girl', 'is', 'human'])
    center.think()
    center.get_wording(['human', 'is', 'mammal'])
    center.think()
    center.get_wording(['?', 'girl', 'mammal'])
    res = center.think()
    print(res)


    center.get_wording(['Cindy', 'is', 'girl'])
    center.think()
    center.get_wording(['?', 'Cindy', 'mammal'])
    res = center.think()
    print(res)

    pass

if __name__ == '__main__':
    main()









