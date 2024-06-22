class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("must implement in subclass")

        def __eq__(self, other) -> bool:
            return self.element == other

        def __ne__(self, other) -> bool:
            return not (self.element == other)

    def root(self):
        raise NotImplementedError("must implement in subclass")

    def parent(self, p):
        raise NotImplementedError("must implement in subclass")

    def num_children(self, p):
        raise NotImplementedError("must implement in subclass")

    def children(self, p):
        raise NotImplementedError("must implement in subclass")

    def len(self):
        raise NotImplementedError("must implement in subclass")

    #!___Implemented code ___________________
    def is_root(self, p):
        return self._root == p

    def is_empty(self):
        return self.len() == 0

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def height(self, p=None):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(c) for c in self.children(p))

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    #!__lec 10 ___
    #!___ positions -- iter ___
    def iter(self):
        return self.positions()

    def positions(self):
        return self.preorder()

    def preorder(self):
        if not self.is_empty():
            for p in self._preorder_recur(self.root()):
                yield p

    def _preorder_recur(self, p):
        yield p
        for c in self.children(p):
            for other in self._preorder_recur(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._postorder_recur(self.root()):
                yield p

    def _postorder_recur(self, p):
        for c in self.children(p):
            for other in self._postorder_recur(c):
                yield other
        yield p

    #!8.4
    def compute_height_for_every_position(self):
        for p in self.positions():
            h = self.height(p)
            print(f"Position ({p.element()}) = {h} h")

    #! inorder is only implemented in Binary Tree


class BinaryTree(Tree):
    def left(self, p):
        """return the position of the left child of Position p in s Tree"""
        raise NotImplementedError("must implement in subclass")

    def right(self, p):
        """return the position of the right child of Position p in s Tree"""
        raise NotImplementedError("must implement in subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None  # the position is root
        if p is self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    

    #!__lec 10__
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
    #!8.8 Easy Answer
    def preorder_next(self,p):
        lst = list(self.preorder())
        for i in range(len(lst)):
            if lst[i].element() == p:
                if i + 1 < len(lst):
                    return lst[i + 1]._node
                else:
                    return None    
        return None
    def inorder_next(self,p):
        lst = list(self.inorder())
        for i in range(len(lst)):
            if lst[i].element() == p:
                if i + 1 < len(lst):
                    return lst[i + 1]._node
                else:
                    return None    
        return None
    
    def postorder_next(self,p):
        lst = list(self.postorder())
        for i in range(len(lst)):
            if lst[i].element() == p:
                if i + 1 < len(lst):
                    return lst[i + 1]._node
                else:
                    return None    
        return None
    
    #!8.8 old answers 
    # def preorder_next(self,p):
    #     return self._preorder_next_subtree(self.root(),p)
    # def _preorder_next_subtree(self, p, e):
    #     if p is None:
    #         return None
    #     if p.element() == e:
    #         if self.left(p) is not None:
    #             return self.left(p)
    #         if self.right(p) is not None:
    #             return self.right(p)
    #         return None
    #     left_result = self._preorder_next_subtree(self.left(p), e)
    #     if left_result is not None:
    #         return left_result
    #     right_result = self._preorder_next_subtree(self.right(p), e)
    #     return right_result


# not LinkedBinaryTree
"""
         A
        / \
        B  C
       / \
       E  F 
"""


class LinkedBinaryTree(BinaryTree):
    class _Node:
        slots = "_element", "_parent", "_right", "_left"

        def __init__(self, element, parent=None, right=None, left=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            if self._node is None:
                return None
            return self._node._element

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("not from the same type")
        if p._container is not self:
            raise ValueError("not in the same container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    #! Accessors
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

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def len(self):
        return self._size

    #! CRUD
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Already has root")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Already there is a child")
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Already there is a child")
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Have 2 childrens can't delete ")
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Already Has a Children")
        if not type(self) is type(t1) is type(t2):
            raise ("They are not the same type value Error")
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

    #!__8.1__
    def get_tree_height(self, p=None):
        if p is None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        left = self.get_tree_height(self.left(p))
        right = self.get_tree_height(self.right(p))
        return 1 + max(left, right)

    #!__8.2__
    def delete_subtree(self, p):
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

    def _subtree_size(self, p):
        node = self._validate(p)
        size = 1
        if node._left is not None:
            size += self._subtree_size(self._make_position(node._left))
        if node._right is not None:
            size += self._subtree_size(self._make_position(node._right))
        return size

    #!__8.3
    def swap(self, p, q):
        # Make sure p and q are valid positions

        # Get the nodes for p and q
        node_p = self._validate(p)
        node_q = self._validate(q)

        # Get the parent nodes of p and q
        parent_p = node_p._parent
        parent_q = node_q._parent

        # Check if p and q are adjacent
        if parent_p is parent_q:
            # Swap the roles of p and q
            if parent_p is not None:
                # swap
                if parent_p._left is node_p:
                    parent_p._left, parent_p._right = node_q, node_p
                else:
                    parent_p._right, parent_p._left = node_q, node_p
            else:
                self._root = node_q
        else:
            # Swap the roles of p and q
            if parent_p is not None:
                if parent_p._left is node_p:
                    parent_p._left = node_q
                else:
                    parent_p._right = node_q
            else:
                self._root = node_q

            if parent_q is not None:
                if parent_q._left is node_q:
                    parent_q._left = node_p
                else:
                    parent_q._right = node_p
            else:
                self._root = node_p

            # Update the parent pointers
            node_p._parent = parent_q
            node_q._parent = parent_p

            # # update children
            # node_p._left, node_q._left = node_q._left, node_p._left
            # node_p._right, node_q._right = node_q._right, node_p._right

    #!__8.4__ should be added to Tree

    #!__8.5__
    def insertBST(self, k, T=None):
        if T is None:
            T = LinkedBinaryTree()
        self.insertBST_recur(k, T.root())
        return T

    def insertBST_recur(self, k, T):
        # if tree is Empty
        if T is None:
            return self._add_root(k)
        else:
            if k < T.element():
                left = self.left(T)
                if left is None:
                    return self._add_left(T, k)
                else:
                    return self.insertBST_recur(k, left)
            else:
                right = self.right(T)
                if right is None:
                    return self._add_right(T, k)
                else:
                    return self.insertBST_recur(k, right)

    #!8.6
    def tree_from_array(self, lst):
        T = LinkedBinaryTree()
        T._add_root(lst[0])
        self.tree_array_recur(lst, T)
        return T

    def tree_array_recur(self, lst, T, index=1):
        if index >= len(lst):
            print()
            return
        T.insertBST(lst[index], T)
        return self.tree_array_recur(lst, T, index + 1)

    #!8.7
    @staticmethod
    def sorted_array_to_bst(arr):
        def _sorted_sub_tree_to_bst(sub_arr,tree,parent,is_left):
            if not sub_arr :
                return None
            mid = len(sub_arr) //2
            element = sub_arr[mid]
            if parent is None:
                new_pos = tree._add_root(element)
            else:
                if is_left:
                    new_pos = tree._add_left(parent,element)
                else:
                    new_pos = tree._add_right(parent,element)

            _sorted_sub_tree_to_bst(sub_arr[:mid],tree,new_pos,True)
            _sorted_sub_tree_to_bst(sub_arr[mid+1:],tree,new_pos,False)

        tree = LinkedBinaryTree()
        _sorted_sub_tree_to_bst(arr,tree,None,True)
        return tree
    #!8.8 implemented in Binary Tree

    

T = LinkedBinaryTree()
root = T._add_root(1)
print(f"Root : {root.element()}")
print(f"length : {T.len()}")
l = T._add_left(root, "B")
r = T._add_right(root, 3)
print(f"right child root : {l.element()}")
print(f"left child root : {l.element()}")
ll = T._add_right(l, 2)
print(f"Right of root is Leaf {T.is_leaf(l)}")
print(f"left child of root : {ll.element()}")
print(f"length : {T.len()}")

old_root = T.replace(root, 100)
root = T.root()
print(f"Replaced root : {old_root}")
print(f"New root : {root.element()}")
deleted_ll = T.delete(l)
print(f"old child {deleted_ll} left child of root : {T.left(root).element()}")

t1 = LinkedBinaryTree()
t1root = t1._add_root(10)
t1._add_left(t1root, 20)
t1._add_right(t1root, 30)


t2 = LinkedBinaryTree()
t2root = t2._add_root(11)
t2._add_left(t2root, 22)
t2._add_right(t2root, 33)
T.attach(ll, t1, t2)
print(f"Size of Sub tree : {T._subtree_size(ll)}")
print(f"New Subtree of {ll.element()} ")
print(f"parent Subtree of {T.parent(ll).element()} ")
# print(f"left child -> {T.right(ll).element()}")
# print(f"Right child  -> {T.left(ll).element()}")
# # print(f"t1 Tree Root : {t1.root().element()}")
# # print(f"t1 Tree : {t2.get_tree_height()}")
# # print(f"t2 Tree : {t2.get_tree_height()}")
# print(f"T Tree : {T.get_tree_height()}")
# print(f"T Tree length before delete {T.len()}")
# print(f"parent of ll {T.parent(ll).element()}")
# T.delete_subtree(T.left(ll))
print(f"T root length after delete : {T.len()}")
# print(f"Right of ll : {T.left(ll).element()}")
newLLL = T.left(ll)
newLLR = T.right(ll)
print(f"Root -> {ll.element()} Right-> {newLLR.element()} , Left -> {newLLL.element()}")
print("Tree in preorder Traversal before swap: ")
for p in T.preorder():
    print(p.element(), end="\t")
#! 20      10      30      D       22      11      33      H       C
#!8.3 method swap(p,q)
T.swap(T.left(root), T.right(newLLR))
print()
print("Tree in preorder Traversal after swap: ")
for p in T.preorder():
    print(p.element(), end="\t")
print()
#!8.4 Give an efficient algorithm that computes and prints, for every position p of a tree T, the
#! element of p followed by the height of p’s subtree.

T.compute_height_for_every_position()

#!8.5 insert Bst
T = T.insertBST(300, T)
print(f"return the Tree where the key inserted : {T.root().element()}")
print(T.right(T.right(root)).element())
print("Tree in preorder Traversal after insertBST: ")
for p in T.preorder():
    print(p.element(), end="\t")
print()


#! 8.6 create tree from unsorted array
lst = [5, 2, 8, 1, 3, 7, 9]
T_lst = T.tree_from_array(lst)
print("Tree in preorder Traversal after unsorted array creation: ")
for p in T_lst.preorder():
    print(p.element(), end="\t")
print()

#! 8.7  create a balanced Binary Search Tree (BST) using a given array elements, where array elements are sorted in ascending order
sorted_lst = [1, 2, 3, 4, 5, 6, 7]
sorted_tree = LinkedBinaryTree.sorted_array_to_bst(sorted_lst)
print("Tree in preorder Traversal after sorted array creation: ")
for p in sorted_tree.inorder():
    print(p.element(), end="\t")
print()

#!8.8
print(f"preorder_next : {sorted_tree.inorder_next(4)._element}")