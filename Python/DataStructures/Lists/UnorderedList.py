class Node(object):
    "Node that holds data and has pointer to next item"

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class List(object):
    "Unordered list data structure"

    def __init__(self):
        self.head = None

    def add(self, item):
        new_item = Node(item)
        new_item.set_next(self.head)
        self.head = new_item

    def remove(self, item):
        pass

    def search(self, item):
        pass

    def is_empty(self):
        return self.head is None

    def size(self):
        pass

    def append(self, item):
        new_node = Node(item)
        if self.head:
            start = self.head
            curr = start
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(new_node)
            self.head = start
        else:
            self.head = new_node


    def index(self, item):
        pass

    def insert(self, pos,item):
        pass

    def pop(self):
        pass

    def pop(self, pos):
        pass

    def __str__(self):
        curr = self.head
        str = '['
        while curr:
            str += curr.get_data().__str__()
            if curr.get_next():
                str += ', '
            curr = curr.get_next()
        str += ']'
        return str

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.get_data()
            curr = curr.get_next()

if __name__ == '__main__':
    l = List()
    l.add(1)
    l.add(2)
    l.add(3)
    print l

    for i in l:
        print i
