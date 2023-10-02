# Post Order Traversal

from index import BST

tree = BST()
vals = [5, 3, 8, 1, 2, 11]
for val in vals:
  tree.insert(val)

#                     5
#                   /   \
#                  3     8
#                /        \
#               1          11
#                \
#                 2
# post order follows the left-right-root policy
# a depth first traversal

def postorder(root):
  if root is None: return
  postorder(root.left)
  postorder(root.right)
  print(root.val)

def postorder_iter(root):
  stack, visited = [], set()
  curr = root
  
  while True:
    while curr.left and curr.left not in visited:
      stack.append(curr)
      curr = curr.left

    if curr.right and curr.right not in visited:
      stack.append(curr)
      curr = curr.right
    else:
      print(curr.val)
      visited.add(curr)
      if not len(stack): break
      curr = stack.pop()

postorder_iter(tree.head)
