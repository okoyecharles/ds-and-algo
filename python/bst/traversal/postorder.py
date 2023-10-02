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
  pass

postorder(tree.head)
