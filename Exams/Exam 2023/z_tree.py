class Tree:
    class Position:
        def element(self):
            raise NotImplementedError
        def __eq__(self, other):
            raise NotImplementedError
        def __ne__(self, other):
            return not (self == other)
    def root(self):
        raise NotImplementedError
    def parent(self,p):
        raise NotImplementedError
    def is_root(self,p):
        return self.root() == p
    def is_leaf(self,p):
        return self.num_children(p) == 0
    def children(self,p):
        raise NotImplementedError
    def num_children(self,p):
        raise NotImplementedError
    def len(self):
        raise NotImplementedError
    def is_empty(self):
        return self.len() == 0
    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def height(self,p):
        if self.is_leaf(p):
            return 0 
        return max(self.depth(p) for p in self)
class BinaryTree(Tree):
    def left(self):
        raise NotImplementedError
    def right(self):
        raise NotImplementedError
    def sibling(self,p):
        parent = self.parent(p)
        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element' , '_parent' , '_left' , '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node
    def _make_position(self, node):
        return self.Position(self,node) if node is not None else None
    def __init__(self) -> None:
        self._root = None
        self._size= 0 

    def root(self):
        if self.is_empty():
            raise ValueError('Tree is empty')
        return self._make_position(self._root)
    def parent(self,p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def right(self,p):
        node = self._validate(p)
        return self._make_position(node._right)
    def left(self,p):
        node = self._validate(p)
        return self._make_position(node._left)
    def num_children(self, p):
        count = 0 
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    def _add_root(self,e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)
    def len(self):
        return self._size
    def _add_left(self,p,e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self._Node(e,node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self,p,e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self._Node(e,node)
        self._size += 1
        return self._make_position(node._right)
    def replace(self,p,e):
        node = self._validate(p)
        old = node._element
        node._element = e 
        return old
    def delete(self,p):
        node = self._validate(p)
        if self.num_children(p) == 2 :
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child.parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent 
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -=1 
        node._parent = node
        return node._element
    

#! IV) 
#! 1- getMin()

    def preorder(self):
        if not self.is_empty():
            for p in self.preorder_recur(self.root()):
                yield p 
    def preorder_recur(self,p):
        yield p 
        for c in self.children(p):
            for other in self.preorder_recur(c):
                yield other
    def getMin(self):
        minmum = self._root._element
        for p in self.preorder():
            if minmum > p.element():
                minmum = p.element()
        return minmum    
    def insertBst(self,k,T):
        if T is None:
            T = LinkedBinaryTree()
        self.insertBst_recur(T.root(),k,T)
        return T
    def insertBst_recur(self,p,k,T):
        if p is None:
            return T._add_root(k)
        else:
            if k < p.element() : 
                if T.left(p) is None:
                    return T._add_left(p,k)
                else:
                    return T.insertBst_recur(T.left(p),k,T)
            else:
                if T.right(p) is None:
                    return T._add_right(p,k)
                else:
                    return T.insertBst_recur(T.right(p),k,T)
                   
T = LinkedBinaryTree()
root = T._add_root(100)
Lroot = T._add_left(root,2)
Rroot = T._add_right(root,3)
Lleft = T._add_left(Lroot,4)
Lright = T._add_right(Lroot,5)
Rleft = T._add_left(Rroot,6)
Rright = T._add_right(Rroot,7)
T = T.insertBst(300,T)
print(T.getMin())
for p in T.preorder():
    print(p.element(),end = ' ')
print()
T = T.insertBst(0,T)

print(T.getMin())
for p in T.preorder():
    print(p.element(),end = ' ')
