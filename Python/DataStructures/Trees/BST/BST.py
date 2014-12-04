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

    def min(self):
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def max(self):
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    def inorder(self):
        curr = self.root
        stack = []
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    yield curr.data
                    curr = curr.right

if __name__ == '__main__':
    import random
    bst = BST()
    test_list = range(10)
    random.shuffle(test_list)
    for i in test_list:
        bst.insert(i)
    print list(bst.inorder())
