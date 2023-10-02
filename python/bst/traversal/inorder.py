# Inorder Traversal

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
# inorder traversal prints numbers in sorted order
# ie: 1 2 3 5 8 11

def inorder(root):
  if root is None: return
  inorder(root.left)
  print(root.val)
  inorder(root.right)

def inorder_iter(root):
  curr = root
  stack = []

  while True:
    while curr:
      stack.append(curr)
      curr = curr.left

    if not len(stack): return
    curr = stack.pop()
    print(curr.val)
    curr = curr.right
    
inorder(tree.head)
