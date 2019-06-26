
class List:
    head = tail = None

    def Add(self, data=None):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def Print(self):
        p = self.head
        while p is not None:
            p.Print()
            p = p.next

    def PrintBack(self):
        p = self.tail
        while p is not None:
            p.Print()
            p = p.prev


class Node:
    data = None
    prev = next = None

    def __init__(self, data=None):
        self.data = data

    def Print(self):
        print(self.data)

