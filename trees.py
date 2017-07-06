def make_tree(label, branches = []):
	"""A (sub)tree with given LABEL at its root, whose children are KIDS."""
	return (label, branches)
def label(tree):
	"""The label on TREE."""
	return tree[0]
def branches(tree):
	"""The children of TREE (each a tree)."""
	return tree[1]
def isleaf(tree):
	"""True if TREE is a leaf node."""
	return len(branches(tree)) == 0
