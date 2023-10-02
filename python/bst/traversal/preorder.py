# Preorder Traversal

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
# preorder traversal follows root-left-right policy
# ie: 5 3 1 2 8 11
def preorder(root):
  if root is None: return
  print(root.val)
  preorder(root.left)
  preorder(root.right)

def preorder_iter(root):
  stack = [root]

  while len(stack):
    curr = stack.pop()
    print(curr.val)

    if curr.right: stack.append(curr.right)
    if curr.left: stack.append(curr.left)

preorder(tree.head)
