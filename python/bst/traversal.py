from index import BST

tree = BST()
vals = [5, 3, 8, 1, 2, 11]
for val in vals:
  tree.insert(val)

# inorder traversal prints numbers in sorted order
def inorder(root):
  if root is None: return
  inorder(root.left)
  print(root.val)
  inorder(root.right)

def inorder_iter(root):
  stack = [root]
  visited = set()
  visited.add(root)
  curr = root

  while len(stack):
    while curr.left and not curr.left in visited:
      curr = curr.left
      stack.append(curr)
      visited.add(curr)

    curr = stack.pop()
    print(curr.val)

    if curr.right:
      curr = curr.right
      stack.append(curr)