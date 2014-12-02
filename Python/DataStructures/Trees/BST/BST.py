class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    "Binary Search Tree"

    def __init__(self):
        self.root = None

    def insert(self, item):
        curr = self.root
        previous = None
        while curr:
            previous = curr
            if item < curr.data:
                curr = curr.left
            elif item > curr.data:
                curr = curr.right
            else:
                break
        if not previous:
            self.root = Node(item)
        else:
            if item < previous.data:
                previous.left = Node(item)
            elif item > previous.data:
                previous.right = Node(item)
            else:
                pass

    def search(self, item):
        curr = self.root
        while curr:
            if item == curr.data:
                return True
            elif item < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

if __name__ == '__main__':
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    print bst.search(2)
