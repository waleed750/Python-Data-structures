class EmptyError(Exception):
    pass
class Tree:
    class Position:
        def element(self):
            raise NotImplemented("Not Implemented Error ")
    def root(self):
        raise NotImplemented("Not Implemented Error ")
    def parent(self,p):
        raise NotImplemented("Not Implemented Error ")
    def children(self,p):
        raise NotImplemented("Not Implemented Error ")
    def num_children(self,p):
        raise NotImplemented("Not Implemented Error ")
    def len(self):
        raise NotImplemented("Not Implemented Error ")
    def is_empty(self):
        return self.len() == 0
    def is_leaf(self,p):
        return self.num_children(p) == 0
    def is_root(self,p):
        return self.root() == p
    def height(self,p):
        if self.is_leaf(p):
            return 0 
        return 1 + max(self.height(c) for c in self.children(p))
    def depth(self,p):
        if self.is_root(p):
            return 0 
        return 1 + self.depth(self.parent(p))
    def get_tree_height(self,p=None):
        if p is None:
            p = self.root()
        
class BinaryTree(Tree):
    def left(self):
        raise NotImplemented("Not Implemented Error ")
    def right(self):
        raise NotImplemented("Not Implemented Error ")
    def sibling(self,p):
        parent= self.parent(p)
        if parent.left() == p :
            return parent.left()
        else:
            return parent.right
    def children(self,p):
        if self.right(p) is not None:
            yield self.right(p)
        if self.left(p) is not None:
            yield self.left(p)
