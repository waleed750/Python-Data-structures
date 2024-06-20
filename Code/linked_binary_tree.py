from tree import Tree , BinaryTree
class LinkedBinaryTree(BinaryTree):
    class _Node:
        slots = '_element', '_parent', '_left', '_right'
        def __init__(self,element,parent=None,left=None,right=None) :
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._container = container
            self._node = node
        def element(self):
            if self._node._element is None:
                return None
            return self._node._element
    #!____________________validation and position _____________________________________
    def _validate(self,p):
        if not isinstance(p,self.Position): raise TypeError("Not the same type")
        if p._container is not self: raise ValueError("Not in the same container")
        if p._node._parent is p._node: raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        return self.Position(self,node) if node is not None else None
    def __init__(self):
        self._root = None
        self._size = 0
    def len(self):
        return self._size
    def root(self):
        return self._make_position(self._root)
    def parent(self,p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count +=1 
        if node._right is not None:
            count += 1
        return count
    def _add_root(self,e):
        if self._root is not None:
            raise ValueError('Root Exists')
        self._root = self._Node(e)
        self._size = 1 
        return self._make_position(self._root)
    def _add_right(self,p,e):
        node = self._validate(p)
        if node._right is not None: raise ValueError("ALREADY RIGHT CHILD EXISTS ")
        node._right = self._Node(e,node)
        self._size +=1
        return self._make_position(node._right)
    
    def _add_left(self,p,e):
        node = self._validate(p)
        if node._left is not None: raise ValueError("ALREADY left CHILD EXISTS ")
        node._left = self._Node(e,node)
        self._size +=1
        return self._make_position(node._left)
    def _replace(self,p,e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    def _delete(self,p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("Postion  contains 2 children ")
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node ## convention for deprecated node
        return node._element
    def attach(self,p,t1,t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("Already Has a Children")
        if not type(self) is type(t1) is type(t2): raise TypeError("Tree types must match")
        self._size += t1.len() + t2.len()
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0 
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._size = 0 
            t2._root = None
    def delete_subtree(self,p):
        # make sure to minus the size and delete all nodes 
        node = self._validate(p)
        subtree_size = self._subtree_size(p)
        if node is self._root:
            self._root = None
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = None
            else:
                parent._right = None
            self._size -= subtree_size
        return subtree_size
    def _subtree_size(self,p):
        node = self._validate(p)
        size = 1
        if node._left is not None:
            size += self._subtree_size(self._make_position(node._left))
        if node._right is not None:
            size += self._subtree_size(self._make_position(node._right))
        return size
# Usage of the LinkedBinaryTree
if __name__ == "__main__":
    T = LinkedBinaryTree()
    root = T._add_root(10)
    l = T._add_left(root, 8)
    r = T._add_right(root, 15)

    print("Tree Size:", T.len())
    print("Number of root's children:", T.num_children(root))
    print("Root element:", T.root().element())
    print("Root left element:", T.left(root).element())
    print("Root right element:", T.right(root).element())
    print("Number of children of root's left child:", T.num_children(l))
    print("Number of children of root's right child:", T.num_children(r))

    ll = T._add_left(l, 4)
    lr = T._add_right(l, 9)

    print("Tree Size:", T.len())
    print("Root left left element:", T.left(l).element())
    print("Root left right element:", T.right(l).element())
    print("Deleted Root left right element:", T._delete(lr))
    print("Deleted right of the root : ",T._delete(r))
    print("Tree Size:", T.len())
    print(f"ll parent : {T.parent(ll).element()}")
    old = T._replace(root, 12)
    print("Root element:", old, "replaced by:", T.root().element())


    t1 = LinkedBinaryTree()
    t1root = t1._add_root(10)
    t1._add_left(t1root,20)
    t1._add_right(t1root,30)


    t2 = LinkedBinaryTree()
    t2root = t2._add_root(11)
    t2._add_left(t2root,22)
    t2._add_right(t2root,33)
    T.attach(ll,t1,t2)


    # T.delete_subtree(T.left(ll))
    print(f"T root length after delete : {T.len()}")
    # print(f"Right of ll : {T.left(ll).element()}")
    print("Tree in postorder Traversal : ")
    for p in T.preorder():
        print(p.element(),end="\t")



