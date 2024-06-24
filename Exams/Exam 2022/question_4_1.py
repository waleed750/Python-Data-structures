# 1- Add to class LinkedBinary Tree the following two methods:
# a) Method get_tree_height(), which calculates the height of i binary tree.
# where:
#       height of a node = max(height of lefi subtree, height of right subtree) + 1
def get_tree_height(self,p=None):
    if p is None:
        p = self.root()
    return self.height(p)

# b) Method countNonLeaves(), which returns the number of non-leaf nodes in a binary tree.

def preorder(self):
    if not self.is_empty():
        for p in self.preorder_recur(self.root()) :
            yield p 
def preorder_recur(self,p):
    yield p 
    for c in self.children(p):
        for other in self.preorder_recur(c):
            yield other
