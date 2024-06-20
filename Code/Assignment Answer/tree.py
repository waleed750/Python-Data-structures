class Tree:
    class Position:
        def element(self):
            '''return the element of the current position'''
            raise NotImplementedError()
        def __eq__(self,other):
            '''return True if element equal to other'''
            return (self.element == other)
        def __ne__(self, other) :
            '''return false if element equal to other'''
            return not (self.element == other)
    def root(self):
        '''return Position of return the Tree s root None if Tree is empty else return the root'''
        raise NotImplementedError
    def parent(self,p):
        '''return position representing p s parent (or None if p is root )'''
        raise NotImplementedError("Implement in subclass")
    def children(self):
        '''return iteration of positions of s Tree'''
        raise NotImplementedError("Implement in subclass")
    def num_children(self,p):
        '''return the number of children that position p has '''
        raise NotImplementedError("Implement in subclass")
    def len(self):
        '''return the length of the s Tree'''
        raise NotImplementedError("Implement in subclass")
    def is_root(self,p):
        return self.root() == p
    def is_leaf(self,p):
        return self.num_children(p) == 0
    def is_empty(self,p):
        return self.len() == 0
    def height(self,p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(c) for c in self.children(p))
    def depth(self,p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))


class BinaryTree(Tree):
     # ---------------------additional abstract methods --------------------
    def left(self, p):
        """Return a Position representing p s left child.
        Return None if p does not have a left child.  """
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        """Return a Position representing p s right child.
        Return None if p does not have a right child.  """
        raise NotImplementedError('must be implemented by subclass') 
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None # the position is root
        if p == self.left(parent):
            return self.right(parent)
        else :
            self.left(parent)
    
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


