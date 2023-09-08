# Trie (Prefix Tree)

class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False

	def insert(self, word):
		curr, i = self, 0
		while i < len(word):
			if word[i] not in curr.children:
				curr.children[word[i]] = TrieNode()	
			curr = curr.children[word[i]]
			i = i + 1		
		curr.end = True

	def has(self, word):
		curr, i = self, 0
		while i < len(word):
			if word[i] not in curr.children:
				return False
			curr, i = curr.children[word[i]], i + 1
		return curr.end

	def startsWith(self, word):
		curr, i = self, 0
		while i < len(word):
			if word[i] not in curr.children:
				return False
			curr, i = curr.children[word[i]], i + 1
		return True
		

trie = TrieNode()
words = ['hey', 'herb', 'cool', 'dog', 'coat']
for word in words:
	trie.insert(word)

test = ['hey', 'herb', 'cool', 'dog', 'coat', 'car', 'do', 'her', 'cool', '', 'c']
