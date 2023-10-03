# Linked Lists

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def __len__(self):
    return self.length

  def print(self):
    linked_list = []
    curr = self.head

    while curr:
      linked_list.append(curr.val)
      curr = curr.next
    print(linked_list)

  def insert(self, val):
    node = ListNode(val)
    curr = self.head
    self.length += 1

    if curr is None:
      self.head = node
      return

    while curr.next:
      curr = curr.next
    curr.next = node
