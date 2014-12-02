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
        curr = self.head
        previous = None
        while curr:
            if curr.get_data() == item:
                if previous:
                    previous.set_next(curr.get_next())
                else:
                    self.head = self.head.get_next()
            previous = curr
            curr = curr.get_next()

    def search(self, item):
        curr = self.head
        while curr:
            if curr.get_data() == item:
                return True
        return False

    def is_empty(self):
        return self.head is None

    def size(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.get_next()
        return length

    def append(self, item):
        new_node = Node(item)
        if self.head:
            curr = self.head
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(new_node)
        else:
            self.head = new_node

    def index(self, item):
        count = 0
        curr = self.head
        while curr:
            if curr.get_data() == item:
                return count
            else:
                count += 1
                curr = curr.get_next()
        return -1

    def insert(self, pos, item):
        curr = self.head
        previous = None
        while pos > 0:
            previous = curr
            curr = curr.get_next()
            pos -= 1
        new_node = Node(item)
        previous.set_next(new_node)
        new_node.set_next(curr)

    def pop(self, pos=None):
        curr = self.head
        previous = None
        if pos:
            while pos > 0:
                previous = curr
                curr = curr.get_next()
                pos -= 1
        else:
            while curr.get_next():
                previous = curr
                curr = curr.get_next()
        previous.set_next(curr.get_next())
        return curr.get_data()

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

    print "Length: ", l.size()

    l.remove(2)
    print l
    print "3 is at index: ", l.index(3)

    l.insert(1, 7)
    print l

    print l.pop(1)
    print l
