# Traversals (inorder, preorder, postorder)

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

inorder_iter(tree.head)

# preorder traversal follows root-left-right pattern
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

def postorder(root):
	if root is None: return
	postorder(root.left)
	postorder(root.right)
	print(root.val)

def postorder_iter(root):
	pass
