# Reverse LinkedList
from index import LinkedList

#          ll: 1 -> 2 -> 3 -> 4 -> 5
# reverse(ll): 5 -> 4 -> 3 -> 2 -> 1

def reverse(ll):
  top = ll
  prev, curr = None, ll.head

  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    
  top.head = prev

ll = LinkedList()
for i in range(1, 1_000):
  ll.insert(i)
reverse(ll)
ll.print()

