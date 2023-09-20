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

# preorder traversal follows root-left-right pattern
# ie: 5 3 1 2 8 11

def preorder(root):
	if root is None: return
	print(root.val)
	preorder(root.left)
	preorder(root.right)

def preorder_iter(root):
	curr = root
	stack = [root]
	visited = set()
	
	while len(stack):
		if curr not in visited:
			print(curr.val)
			visited.add(curr)

		if curr.left and curr.left not in visited:
			curr = curr.left
			stack.append(curr)
		else:
			curr = stack.pop()
			if curr.right:
				curr = curr.right
				stack.append(curr)

