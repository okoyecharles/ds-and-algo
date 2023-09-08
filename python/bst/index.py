# Binary Search Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        def search_and_insert(head):
            if val >= head.val:
                if not head.right:
                    head.right = node
                else:
                    search_and_insert(head.right)
            else:
                if not head.left:
                    head.left = node
                else:
                    search_and_insert(head.left)

        # search for position and insert the value in tree
        search_and_insert(self.head)

    def exists(self, val):
        def search(head):
            if not head:
                return False
            if head.val == val:
                return True

            if val >= head.val:
                return search(head.right)
            else:
                return search(head.left)

        return search(self.head)