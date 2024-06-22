class ArrayBinaryTree:
    class _Node:
        __slots__ = '_element', '_parent' , '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    class Position:
        def __init__(self, node, index) -> None:
            self._node = node
            self._index = index

        def element(self):
            return self._node._element

    def __init__(self):
        self._data = [None] * 10
        self._root = 0
        self._size = 0

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def root(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        return self._data[self._root]

    def left(self, p):
        index = (2 * p._index) + 1
        if index >= len(self._data):
            return None
        return self._data[index]

    def right(self, p):
        index = (2 * p._index) + 2
        if index >= len(self._data):
            return None
        return self._data[index]
    def parent(self,p):
        if p._index >= len(self._data):
            raise ValueError("index out of range")
        return p._node._parent._element
    def _add_root(self, e):
        if self._data[self._root] is not None:
            raise ValueError("Tree is not empty")
        self._data[self._root] = self.Position(self._Node(e), self._root)
        self._size += 1
        return self._data[self._root]

    def _add_left(self, p, e):
        index = (2 * p._index) + 1
        if index >= len(self._data):
            self._resize
        node = self._Node(e,p._node,)
        self._data[index] = self.Position(node, index)
        self._size += 1
        return self._data[index]
    def _add_right(self, p, e):
        index = (2 * p._index) + 2
        if index >= len(self._data):
            self._resize
        node = self._Node(e,p._node,)
        self._data[index] = self.Position(node, index)
        self._size += 1
        return self._data[index]


    def _resize(self):
        self._data += [None] * 10

    def delete(self, p: Position):
        if p._index >= len(self._data):
            raise ValueError("index out of range")
        old = self._data[p._index].element()
        self._data.pop(p._index)
        self._size -= 1
        return old
    def children(self, p):
        if p._index >= len(self._data):
            raise ValueError("index out of range")
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    def positions(self):
        if not self.is_empty():
            for p in self.preorder(self.root()):
                yield p         
    def preorder(self,p):
        yield p
        for c in self.children(p):
            for other in self.preorder(c):
                yield other


def main():
    AT = ArrayBinaryTree()
    root = AT._add_root(10)
    r_root = AT._add_right(root, 12)
    l_root = AT._add_left(root, 11)
    print(f"Root of the tree : {root.element()}")
    print(f"Roo Right child :{r_root.element()}")
    # print(f"Root of the tree : {AT.left(r_root).element()}")
    print(f"Size of the tree : {AT.len()}")
    # print(AT._data)
    ll = AT._add_left(l_root, 13)
    lr = AT._add_right(l_root, 14)
    print(f"Left child of root:{ll.element()}")
    print(f"Right child of root:{lr.element()}")

    print(f"Size of the tree : {AT.len()}")
    AT.delete(ll)
    print("Tree : ")
    for p in AT.positions():
        print(p.element(),end = " ")

    print("Parent of root : ",AT.parent(r_root))
main()