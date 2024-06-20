from tree import BinaryTree
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
            return self._node._element
    #!____________________validation and position _____________________________________
    def _validate(self,p):
        if not isinstance(p,self.Position): raise TypeError("Not the same type")
        if p._container is not self: raise ValueError("Not in the same container")
        if p._node._parent is p._node: raise ValueError("inconvinet parent")
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
            if node == parent._left:
                parent._left = child
            else:
                parent._right = child
            self._size -= 1
            node._parent = node ## convention for deprecated node
            return node._element
        
    #!_________________________________Answer_____________________________________________
    def print_the_tree(self,p):
        if p is not None:
            right = self.right(p).element() if self.right(p) is not None else None
            left = self.left(p).element() if self.left(p) is not None else None
            print(f"{p.element()} -> Left: {left}, Right: {right}")
            self.print_the_tree(self.right(p))
            self.print_the_tree(self.left(p))

    #!__8.1___
    def _height(self,p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(sub) for sub in self.children(p))
    def get_tree_height(self,p=None):
        if p is None:
            p = self._make_position(self._root)
        return self._height(p)
    #!__8.2___
    def count_sub_tree(self,p):
        if p is None:
            return 0
        left_count = self.count_sub_tree(self.left(p))
        right_count = self.count_sub_tree(self.right(p))
        return 1 + right_count + left_count
    def delete_sub_tree(self,p):
        if self.left(p) is not None:
            self.delete_sub_tree(self.left(p))
        if self.right(p) is not None:
            self.delete_sub_tree(self.right(p))
        p._node._parent = p._node._left = p._node._right = None
    def  _delet_sub_tree(self,p):
        if p.parent:
            if p.parent.left == p:
                p.parent.left = None
            else:
                p.parent.right = None
        node = self._validate(p)
        self._size -= self.count_sub_tree(p)
        self.delete_sub_tree(p)
    #!__8.3___
    


        

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
print("Tree Size:", T.len())

old = T._replace(root, 12)
print("Root element:", old, "replaced by:", T.root().element())

cl = T._add_left(ll,20)
cr = T._add_right(ll,30)
print(f"Element at position {T.parent(cl).element()}: {T.left(ll).element()} ")

print("height : ",T.get_tree_height())
print(f"count sub Tree : {T.count_sub_tree(T.root())}")
#!8.2 delete position
deletedPosition = T.parent(cl).element()
T.delete_sub_tree(ll)
print(f"count sub Tree after deleting {deletedPosition} : {T.count_sub_tree(T.root())}")

T.print_the_tree(T.root())
