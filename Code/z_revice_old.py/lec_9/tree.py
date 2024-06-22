class Tree:
    class Position:
        def element(self):
            raise NotImplemented("must be implemented in subclass")
        def __eq__(self, other) :
            raise NotImplemented("must be implemented in subclass") 
        def __ne__(self,other):
            return not(other == self)
    def root(self):
        raise NotImplemented("must be implemented in subclass") 
    def parent(self,p):
        raise NotImplemented("must be implemented in subclass") 
    def children(self,p):
        raise NotImplemented("must be implemented in subclass") 
    def num_children(self,p):
        raise NotImplemented("must be implemented in subclass") 
    def len(self):
        raise NotImplemented("must be implemented in subclass") 
    def is_empty(self):
        return self.len() == 0
    def is_root(self,p):
        return self.root() == p
    def is_leaf(self,p):
        return self.num_children(p) == 0 
    def height(self,p):
        if self.is_leaf(p):
            return 0 
        return 1 + max(self.height(c) for c in self.children(p))
    def depth(self,p):
        if self.is_root(p):
            return 0 
        return 1 + self.depth(self.parent(p))
    def positions(self):
        if not self.is_empty():
            for p in self.preorder(self.root()):
                yield p
    def preorder(self,p):
        yield p 
        for c in self.children(p):
            for other in self.preorder(c):
                yield other
    def postorder(self,p):
        for c in self.children(p):
            for other in self.preorder(c):
                yield other
        yield p 
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplemented("must be implemented in subclass") 
    def right(self,p):
        raise NotImplemented("must be implemented in subclass") 
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
        __slots__ = '_element' , '_parent', '_left', '_right'
        def __init__(self,element,parent=None,left=None,right=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    class Position(BinaryTree.Position):
        def __init__(self,container, node) -> None:
            self._container = container
            self._node = node
        def element(self):
            if self._node is None:
                return None
            return self._node._element
        def __eq__(self, other) :
            return type(other) is type(self) and other._node is self._node
    def __init__(self):
        self._root = None
        self._size = 0 
    def _validate(self,p:Position):
        if not isinstance(p,self.Position): raise TypeError("p is not type Position")
        if p._container is not  self: raise ValueError("p doesn't belong to this tree")
        if p._node._parent is p._node : raise ValueError("p is not longer valid ") 
        return p._node
    def _make_position(self,node):
        return self.Position(self,node) if node is not None else None
    def root(self):
        return self._make_position(self._root)
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    def len(self):
        return self._size
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._right is not None:
            count += 1 
        if node._left is not None:
            count += 1
        return count
    #! accessor ended 
    def _add_root(self,e):
        if self._root is not None:
            raise ValueError("Root already Existed")
        self._size = 1 
        self._root = self._Node(e)
        return self._make_position(self._root)
    def _add_left(self,p,e):
        node = self._validate(p)
        if node._left is not None: raise ValueError("Left child already Existed ")
        node._left = self._Node(e,node) # node is the parent 
        self._size += 1
        return self._make_position(node._left)
    def _add_right(self,p,e):
        node = self._validate(p)
        if node._right is not None: raise ValueError("Left child already Existed ")
        node._right = self._Node(e,node) # node is the parent 
        self._size += 1
        return self._make_position(node._right)
    #! add functions ended 
    def replace(self,p,e):
        node = self._validate(p)    
        old = node._element
        node._element = e 
        return old 
    def _delete(self,p):
        node = self._validate(p)
        if self.num_children(p) == 2 : raise ValueError("Already have 2 children")
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent # grandfather become parent
        if node._parent is None:
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node# convient deprecated node
        return node._element
    def _attach(self,p,t1 ,t2):
        node = self._validate(p)
        if not self.is_leaf(p) : raise ValueError("Position must be leaf")
        if not type(self) is type(t1) is type(t2): raise TypeError("Trees must be the same type")
        self._size += t1.len() + t2.len()
        if not t1.is_empty():
            node._left = t1._root
            t1._root._parent = node
            t1._size = 0 
            t1._root = None # empty the tree
        if not t2.is_empty():
            node._right = t2._root
            t2._root._parent = node
            t2._size = 0 
            t2._root = None # empty the tree
    def display(self):
        for p in self.positions():
            print(p.element(),end=f"{" "*5}")
        print()
    def get_tree_height(self,p=None):
        if p is None:
            p = self.root()
        return self.height(p)
    #! 8.2 
    def _subtree_size(self,p):
        if p is None:
            return 0 
        return 1+ self._subtree_size(self.left(p)) + self._subtree_size(self.right(p))
    def _delete_subtree(self,p):
        node = self._validate(p)
        subtree_size = self._subtree_size(p)
        if node._parent is None:
            self._root = None
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = None
            else:
                parent._right = None
        node._parent = node._left = node._right = None
        self._size -= subtree_size
        return node._element
    #! 8.3 swap 
    def swap(self,p,q):
        node_p = self._validate(p)
        node_q = self._validate(q)

        parent_p = node_p._parent
        parent_q = node_q._parent
        # swap roles of p , q 
        if parent_p is not None:
            if parent_p._left is node_p:
                parent_p._left = node_q 
            else:
                parent_p._right = node_q 
        else:
            self._root = node_q
        
        if parent_q is not None:
            if parent_q._left is node_q:
                parent_q._left  = node_p
            else:
                parent_q._right = node_p
        else:
            self._root = node_p
        
        #swap children
        node_p._left , node_q._left = node_q._left , node_p._left
        node_p._right , node_q._right = node_q._right , node_p._right

        if node_p._left is not None:
            node_p._left._parent = node_p
        if node_p._right is not None:
            node_p._right._parent = node_p
        if node_q._left is not None:
            node_q._left._parent = node_q
        if node_q._right is not None:
            node_q._right._parent = node_q

        # Swap parents
        node_p._parent, node_q._parent = node_q._parent, node_p._parent

        #!8.5 insertBst
    def insertBst(self,k,T = None):
        if T is None:
            T = LinkedBinaryTree()
        self.insertBst_recur(T.root(),k,T)
        return T
    def insertBst_recur(self,p,k,T):
        if p is None:
            return T._add_root(k)
        elif k < p.element():
            if T.left(p) is None:
                return T._add_left(p,k)
            else:
                return self.insertBst_recur(T.left(p) , k , T)
        else: # k >= p.element()
            if T.right(p) is None:
                return T._add_right(p,k)
            else:
                return self.insertBst_recur(T.right(p) , k , T)
    # def insertBst(self,k,T =None):
    #     if T is None:
    #         T = self
    #     T.insert_recur(T.root(),k, T)
    #     return T
    # def insert_recur(self,p,k,T):
    #     if p is None:
    #         return T._add_root(k)
    #     elif k < p.element():
    #         if self.left(p) is None:
    #             return T._add_left(p,k)
    #         else :
    #             return self.insert_recur(self.left(p),k,T)
    #     else:  # k >= p.element()
    #         if self.right(p) is None:
    #             return self._add_right(p, k)
    #         else:
    #             return self.insert_recur(self.right(p), k,T)
            
    @staticmethod
    def binaryTreeFromArray(lst):
        T = LinkedBinaryTree()
        for i in lst:
            T =  T.insertBst(i,T)
        return T
    @staticmethod
    def sorted_array_to_bst(arr):
        def helper(sub_arr , tree , parent , is_left):
            if not sub_arr :
                return None
            mid = len(sub_arr) // 2
            element = sub_arr[mid]
            if parent is None:
                new_pos = tree._add_root(element)
            else:
                if is_left :
                    new_pos = tree._add_left(parent,element)
                else:
                    new_pos = tree._add_right(parent,element)
            helper(sub_arr[:mid],tree,new_pos,True)
            helper(sub_arr[mid+1:],tree,new_pos,False)
        tree = LinkedBinaryTree()
        helper(elements , tree , None , True)
        return tree

T = LinkedBinaryTree()
root = T._add_root(10)
l = T._add_left(root,20)
r = T._add_right(root,30)
print(f"Subtree size  : {T._subtree_size(root)}")

rl = T._add_left(r,40)
print(f"Height of Tree : {T.get_tree_height()}")

print(f"Root : {root.element()}")
print(f"Left : {l.element()}")
print(f"Right : {r.element()}")
print(f"Size : {T.len()}")
print(f"Subtree size  : {T._subtree_size(root)}")

ll = T._add_right(l,21)

print(f"Left Left : {ll.element()}")
replaced_root = T.replace(root,1)
print("Replaced Root : ",replaced_root , "and new Root : ",root.element())
print("Tree : ",end="")
T.display()
deleted_l = T._delete(l)
print("Deleted Left : ",deleted_l , "and new Left : ",T.left(root).element())

t1 = LinkedBinaryTree()
t1root = t1._add_root(100)
t1l = t1._add_left(t1root,200)
t1r = t1._add_right(t1root,300)

t2 = LinkedBinaryTree()
t2root = t2._add_root(110)
t2l = t2._add_left(t2root,220)
t2r = t2._add_right(t2root,330)
T._attach(ll,t1,t2)
print("Tree : ",end="")
T.display()
print(f"Size of the {T.len()}")
print(f"height : {T.get_tree_height()}")
print(f"Subtree size of {ll.element()} : {T._subtree_size(ll)} ")
print("After deleting sub tree : ",end="")
# p = T._delete_subtree(ll)
# print("Size : ",T.len())
# T.display()
print("After Swaping : ",end=" ")
T.swap(r,ll)
T.display()

for p in T.positions():
    print(f"Position ({p.element()}) , {T.height(p)}")

L = LinkedBinaryTree()
L = L.insertBst(200,L)
L.display()
lst = [25 , 50 , 75 , 100 , 125 , 150]
t_from_lst = LinkedBinaryTree.binaryTreeFromArray(lst)
t_from_lst.display()
print("Size : ", t_from_lst.len())

# sorted array 
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bst = T.sorted_array_to_bst(elements)
bst.display()